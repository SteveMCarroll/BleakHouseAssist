# Bleak House Character Tracker - Architecture Documentation

**Last Updated:** December 7, 2024

## Overview

This is a **pure static web application** that helps readers track characters in Charles Dickens' "Bleak House" (67 chapters). It's designed to reduce the cognitive load of remembering the large cast of characters as the novel progresses.

## Key Architecture Decision: Static Data Generation

**The most interesting aspect of this application is that it uses STATICALLY GENERATED data rather than dynamically processing the novel.**

### Why Static?

1. **Performance**: No server-side processing, no API calls, instant loading
2. **Simplicity**: Just HTML + JavaScript + CSS - can be opened directly from disk
3. **Portability**: Works anywhere, no dependencies, no build process
4. **Offline-first**: Perfect for reading assistance even without internet

### What This Means

All character data, summaries, and relationships are **pre-generated** and stored in `data.js`. The application doesn't parse the novel text at runtime - it simply displays pre-computed information based on user selection.

## File Structure

### Core Application Files (Keep These)

- **`index.html`** - Main application UI with embedded JavaScript
  - Chapter selector (1-67)
  - Character relationship circles visualization
  - Character story modal popup
  - Responsive design for mobile/desktop
  - All application logic is embedded in <script> tags (no separate app.js file)

- **`data.js`** - **THE HEART OF THE APP** - All static data
  - Character lists by chapter
  - Character relationships (grouped into "circles")
  - Chapter summaries (brief context)
  - Character stories (cumulative summaries up to each chapter)
  - All manually curated/AI-generated content
  - Can be rebuilt from chapter_data_backup/ using build_data_js.py

- **`README.md`** - User-facing documentation
- **`PROJECT_SUMMARY.md`** - Development history and context
- **`ARCHITECTURE.md`** - This file

### Development/Build Files

- `test.html` - Testing version for data validation
- `simple-test.html` - Simple data load test
- `build_data_js.py` - Python script to rebuild data.js from backup files

### Source Data Files (Keep for Reference/Updates)

- **`BleakHouse.txt`** - Full novel text (reference for creating summaries)
- **`chapter_data_backup/`** - Directory containing backup data files:
  - `capsule_summaries/` - Brief chapter context summaries (keep for rebuilding)
  - `chapter_summaries/` - Full detailed chapter summaries (keep for rebuilding)
  - `chapter_titles.json` - Chapter titles (keep for rebuilding)
  - `character_appearances/` - Character lists by chapter (keep for rebuilding)
  - `character_stories/` - Character story entries by chapter (keep for rebuilding)

## Data Structure in data.js

```javascript
const BLEAK_HOUSE_DATA = {
    // List of major recurring characters
    majorCharacters: ["Esther Summerson", "Lady Dedlock", ...],
    
    // Display order for relationship circles (most important first)
    circleOrder: ["Bleak House", "Chancery", "Chesney Wold", ...],
    
    // Context for each chapter (brief setting description)
    chapterContext: {
        1: "London, Court of Chancery",
        2: "Lincolnshire, Chesney Wold estate",
        ...
    },
    
    // Chapter titles
    chapterTitles: {
        1: "In Chancery",
        2: "In Fashion",
        ...
    },
    
    // Characters appearing in each chapter, grouped by relationship circle
    charactersByChapter: {
        1: {
            "Chancery": [
                { name: "Lord High Chancellor", summary: "..." },
                ...
            ],
            "Jarndyce": [...],
            ...
        },
        ...
    },
    
    // Full chapter summaries
    chapterSummaries: {
        1: "The chapter opens with a vivid description...",
        ...
    },
    
    // CHARACTER-SPECIFIC CUMULATIVE STORIES
    // This is the key feature that makes the app useful
    characterStories: {
        "Esther Summerson": {
            3: "Narrates her sad childhood: raised by strict godmother...",
            4: "Arrives in London, meets Ada and Richard...",
            5: "Travels to Bleak House. Mr. Jarndyce appoints her housekeeper...",
            ...
        },
        "Mr. Tulkinghorn": {
            2: "The Dedlocks' elderly family lawyer. Shows Lady Dedlock legal papers...",
            8: "Investigates the handwriting. Visits law stationer Snagsby...",
            ...
        },
        ...
    }
};
```

## How It Works

1. **User selects a chapter** (e.g., Chapter 5)
2. **App displays:**
   - Chapter title and context
   - All characters present in that chapter
   - Characters grouped by relationship circles
   - Major characters highlighted
3. **User clicks a character name**
4. **App shows character's cumulative story:**
   - Collects all entries for that character from chapters 1 up to (but not including) the selected chapter
   - Shows what the reader needs to remember about this character
   - Formatted with chapter numbers for reference

## Key Functions

```javascript
// Check if character is major
function isMajorCharacter(characterName)

// Get character data for specific chapter
function getCharactersForChapter(chapter)

// Get cumulative character story up to a chapter
function getCharacterStory(characterName, upToChapter)
```

## Design Philosophy

### User Experience Goals

1. **Non-Spoiler**: Only show information up to the current reading point
2. **Quick Reference**: Help readers remember "Who is this person again?"
3. **Context-Aware**: Show relationships between characters
4. **Progressive Disclosure**: Start simple (chapter view) → dig deeper (character story)

### Visual Design

- **Circles/Grouping**: Characters organized by social circles/locations
- **Color Coding**: Major characters highlighted in gold
- **Responsive**: Works on phones (reading while commuting) and desktops

## Data Generation Workflow

Since data is static, adding content requires:

1. **For new chapters**: Read the chapter, identify characters
2. **Create chapter summary**: Brief paragraph about what happens
3. **Update character stories**: For each character that appears or is mentioned:
   - Add a brief entry for that chapter
   - Focus on: what did they DO? What did we LEARN about them?
4. **Update data.js**: Add entries to appropriate objects
5. **Test**: Load index.html and verify

### Example: Adding Chapter 11

```javascript
charactersByChapter: {
    11: {
        "Bleak House": [
            { name: "Esther Summerson", summary: "Narrator, caring for sick Jo" },
            ...
        ],
        ...
    }
},

characterStories: {
    "Esther Summerson": {
        ...
        11: "Takes in sick Jo despite the risk. Shows her compassionate nature."
    }
}
```

## Technical Requirements

- **Browser**: Any modern browser (Chrome, Firefox, Safari, Edge)
- **No server required**: Just open index.html
- **No build process**: No npm, webpack, etc.
- **JavaScript**: Vanilla ES6+, no frameworks
- **CSS**: Custom CSS, no preprocessors

## Maintenance

### Regular Updates
- Continue adding chapters as they're completed
- Refine character stories based on user feedback
- Add new characters as they appear

### Potential Enhancements
- Search functionality (search for a character)
- Character relationship graphs
- Export reading notes
- Theme customization

### Data Quality
- Character stories should be 2-3 sentences max
- Focus on character-specific actions, not plot summary
- Maintain consistent voice and style
- Verify no spoilers leak into earlier chapters

## Why This Approach Works

1. **Dickens novels are LONG**: 67 chapters, 100+ characters
2. **Serial structure**: Originally published monthly, readers needed reminders
3. **Modern readers**: We don't read serially, but still need help tracking characters
4. **Static is sufficient**: The book doesn't change, so pre-computed data is perfect
5. **Performance**: Instant load, no processing overhead
6. **Privacy**: No data sent to servers, works offline

## Future Considerations

If the project grows beyond Bleak House:

- Could generate data for other Dickens novels
- Template system for adding new books
- AI-assisted summary generation (but human review essential)
- Community contributions for summaries

But the core principle remains: **Static, pre-generated data > Dynamic processing**

---

## Quick Start for Future Development

```bash
# Just open the file
start index.html

# Or on Mac/Linux
open index.html

# To edit data
# 1. Edit data.js directly
# 2. Refresh browser
# 3. No build step!
```

That's it. The simplicity is the power.

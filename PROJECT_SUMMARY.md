# Bleak House Companion - Project Summary

## What This Is
A spoiler-free study guide web app for Charles Dickens' *Bleak House*. Helps readers track characters and plot without revealing future developments.

## How It Works
1. Reader selects their current chapter from dropdown
2. App displays:
   - **Capsule Summary** - 1-2 line chapter overview (NO spoilers) - above character list
   - **Characters by Circle** - All relevant characters organized by their social sphere
   - **Full Chapter Summary** - Detailed plot summary (collapsed by default, for reading AFTER the chapter)
   - **Character Stories** - Click any character name to see their story up to the START of that chapter

## Status

### ✅ Complete (Chapters 1-10)
- Full chapter data with capsule and detailed summaries
- Complete character lists organized by circle
- Character stories that track progression chapter-by-chapter
- Major/minor character distinction
- Mobile-responsive UI

### 🔧 In Progress (Chapters 11-67)
- Chapter contexts and summaries exist (from ollama generation)
- Character data needs to be generated properly
- Use Claude to generate accurate data since I know the book

## Key Files

### Core Application
- **index.html** - Main web page with UI and embedded JavaScript (no separate app.js)
- **data.js** - All chapter and character data (can be rebuilt from backups)

### Data Files
- **chapter_data_backup/** - Backup directory with all source data organized by type
  - capsule_summaries/ - Brief chapter contexts
  - chapter_summaries/ - Full chapter summaries
  - character_appearances/ - Character lists per chapter
  - character_stories/ - Character progression entries
  - chapter_titles.json - All chapter titles
- **BleakHouse.txt** - Full novel text (public domain)

### Scripts
- **build_data_js.py** - Rebuilds data.js from backup files in chapter_data_backup/

## Data Structure

Each chapter in JSON files contains:
```json
{
  "title": "Chapter Title",
  "context": "Brief 1-2 line capsule summary (NO spoilers)",
  "summary": "Full detailed chapter summary (spoiler-full)",
  "characters": {
    "Circle Name": [
      {
        "name": "Character Name",
        "summary": "One-line character description",
        "story": "Character's full story UP TO START of this chapter"
      }
    ]
  }
}
```

**CRITICAL**: The `story` field contains the character's journey UP TO but NOT INCLUDING the current chapter.

## Character Circles (display order)
1. **Bleak House** - Main household
2. **Chesney Wold** - The Dedlocks
3. **Chancery** - Legal system
4. **London Streets** - Street characters
5. **The Bagnets** - Military family
6. **The Smallweeds** - Money-lenders  
7. **Other** - Miscellaneous

## Major Characters
Listed first, more prominent styling: Esther, Ada, Richard, Lady Dedlock, Sir Leicester, Mr. Jarndyce, Mr. Tulkinghorn, Jo, Harold Skimpole

## Important Design Principles
1. **No Spoilers in Capsule**: Context field doesn't reveal chapter events
2. **Character Stories Up To Chapter Start**: Critical for spoiler-free experience
3. **Complete Per-Chapter Data**: Every chapter is self-contained
4. **Named Characters Only**: Skip unnamed mob characters
5. **Mobile-First**: Responsive design for phone reading

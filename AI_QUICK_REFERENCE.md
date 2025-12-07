# AI Quick Reference - Bleak House Character Tracker

**Last Updated:** December 7, 2024

## 30-Second Summary

This is a **static web app** (HTML+JS+CSS) that helps readers track 100+ characters in Dickens' "Bleak House" (67 chapters). All data is **pre-generated** in `data.js` - no dynamic processing. Click character names to see their story up to current reading point (non-spoiler).

## File Overview

```
/
├── index.html          [UI: chapter selector, character circles, modal popups]
├── data.js            [ALL DATA: characters, stories, summaries - 165KB]
├── BleakHouse.txt     [Source: full novel text for reference]
├── README.md          [User docs]
├── ARCHITECTURE.md    [Tech design - READ THIS for architecture details]
└── PROJECT_SUMMARY.md [Dev history]
```

## Key Concept: Static Data Philosophy

**NOT a parser/analyzer**. It's a **pre-computed lookup table**.

```javascript
// User selects Chapter 5
// App shows: characters in Chapter 5
// User clicks "Esther Summerson"  
// App shows: Esther's entries from Chapters 3, 4 (cumulative, non-spoiler)
```

All data manually/AI-curated, stored statically. No text processing at runtime.

## Data Structure (in data.js)

```javascript
BLEAK_HOUSE_DATA = {
    charactersByChapter: {
        5: {
            "Bleak House": [
                {name: "Esther", summary: "..."},
                // who appears in Ch5, by social circle
            ]
        }
    },
    
    characterStories: {
        "Esther Summerson": {
            3: "Brief summary of Esther in Ch3",
            4: "Brief summary of Esther in Ch4",
            // cumulative character-specific info
        }
    },
    
    chapterSummaries: { 1: "Full chapter summary...", ... },
    majorCharacters: ["Esther", "Lady Dedlock", ...],
    // etc.
}
```

## Function: getCharacterStory()

```javascript
function getCharacterStory(characterName, upToChapter) {
    const data = BLEAK_HOUSE_DATA.characterStories[characterName];
    let storyParts = [];
    for (let ch = 1; ch <= upToChapter; ch++) {
        if (data[ch]) {
            storyParts.push(`<p><strong>Ch ${ch}:</strong> ${data[ch]}</p>`);
        }
    }
    return storyParts.join('\n');
}
```

## Common Tasks

### Add a New Chapter (e.g., Chapter 11)

Edit `data.js`:

```javascript
// 1. Add characters who appear
charactersByChapter: {
    11: {
        "Bleak House": [
            {name: "Esther Summerson", summary: "Caring for Jo"},
            ...
        ]
    }
}

// 2. Add character story entries
characterStories: {
    "Esther Summerson": {
        ...
        11: "Takes in sick Jo, shows compassion despite risk."
    },
    "Jo": {
        11: "Falls ill, taken in by Esther at Bleak House."
    }
}

// 3. Add chapter summary
chapterSummaries: {
    11: "Full plot summary of chapter 11..."
}
```

Then refresh `index.html` - no build step!

### Character Story Guidelines

✅ **Good:** "Discovers he is Ada's cousin. Decides to study medicine but lacks commitment."
❌ **Bad:** "Chapter 6: Richard appears and talks to Mr. Jarndyce about his future."

**Rules:**
- 2-3 sentences max
- Character-focused (what THEY did/learned)
- No chapter plot summary
- Cumulative (builds on previous entries)

### Testing

```bash
# Open in browser
start index.html

# Test:
# 1. Select chapter 5
# 2. Click "Esther Summerson"
# 3. Should show entries from chapters 3, 4 only (not 5)
# 4. Entries should be character-specific, not full chapter summaries
```

## Common Issues & Fixes

**Issue:** "Character story shows full chapter summaries"
**Fix:** Character stories should be brief, character-focused. See `characterStories` format above.

**Issue:** "Character story not appearing"
**Fix:** Check `characterStories` object has entry for that character at that chapter number.

**Issue:** "Loading character story..." never finishes
**Fix:** Check browser console for JS errors. Likely data.js syntax error (missing comma, quote, etc.).

## Why This Design?

1. **Dickens = Static**: Book doesn't change, pre-computed data is perfect
2. **Performance**: Instant load, no processing overhead
3. **Simplicity**: No server, no build, no dependencies
4. **Offline**: Works anywhere, perfect for reading assistant
5. **Maintenance**: Easy to update - just edit data.js

## Current Status (Dec 2024)

- ✅ **ALL 67 CHAPTERS COMPLETE!**
- ✅ Character story modal working correctly
- ✅ Non-spoiler design: shows info up to (not including) selected chapter
- ✅ Complete coverage from Chapter 1 to Chapter 67
- ✅ All major plot points, character arcs, and relationships documented

## If You're Fixing Bugs

1. **Check data.js syntax** - most issues are JSON/JS syntax errors
2. **Check browser console** - errors will show there
3. **Test character story modal** - click various characters, verify output
4. **Verify non-spoiler** - viewing Ch5 should NOT show Ch5 info

## If You're Adding Features

The static data model is the constraint and the strength. New features should:
- Use existing data in `data.js` 
- Add new data structures if needed (but keep it static!)
- Not parse `BleakHouse.txt` at runtime (defeats the purpose)

Examples:
- ✅ Search feature: search pre-indexed `characterStories`
- ✅ Character relationships: add `characterRelationships` object to data.js
- ❌ AI chat about book: requires dynamic processing, wrong tool

---

**Remember:** This is an elegant pre-computed lookup table, not a dynamic text analyzer. That's what makes it fast and simple!

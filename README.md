# Bleak House Character Tracker

An interactive web application to help readers track characters while reading Charles Dickens' "Bleak House."

## Quick Start

**Simply open `index.html` in any web browser.** No server, no installation, no build process required!

## Features

- 📖 **Non-Spoiler Design**: Only shows information up to your current chapter
- 🎭 **Character Stories**: Click any character to see their story so far
- 🔄 **Relationship Circles**: Characters organized by social groups and locations
- ⭐ **Major Characters Highlighted**: Easy to spot recurring important characters
- 📱 **Responsive**: Works on phones and desktops
- ⚡ **Fast**: Pure static files, loads instantly

## How to Use

1. **Select a chapter** you're about to read (or just finished)
2. **See all characters** that appear in that chapter, grouped by social circles
3. **Click any character name** to see their cumulative story up to that point
4. **Never get lost** trying to remember "Wait, who is this person again?"

## Character Circles

Characters are grouped by their social worlds:

- **Bleak House**: John Jarndyce's household and wards
- **Chancery**: Legal world and Court of Chancery  
- **Chesney Wold**: The Dedlock family and aristocracy
- **London Poor**: Jo, crossing sweepers, and the destitute
- **Legal London**: Lawyers, law stationers, and the legal trade
- And more as the story progresses...

## Current Coverage

**ALL 67 CHAPTERS COMPLETE!** ✨

The application now includes detailed character information and stories for the entire novel, from the fog-shrouded opening in Chancery to Esther's happy ending seven years later.

## How Character Stories Work

When viewing Chapter N, character stories show **only what you've learned in chapters 1 through N-1**. This prevents spoilers while helping you remember who characters are.

Example: Viewing Chapter 5 and clicking "Esther Summerson" shows her story from Chapters 3-4 only.

## Technical Details

This is a **pure static web application**:
- No backend server required
- No API calls or dependencies
- Just HTML, JavaScript, and CSS
- All data pre-generated in `data.js`

See `ARCHITECTURE.md` for detailed technical documentation.

## Files in This Project

- **`index.html`** - Main application interface (contains all HTML, CSS, and JavaScript)
- **`data.js`** - All character and chapter data (static/pre-generated)
- **`BleakHouse.txt`** - Full novel text (reference material)
- **`chapter_data_backup/`** - Backup data files used to rebuild data.js if needed
- **`build_data_js.py`** - Script to rebuild data.js from backup files
- **`README.md`** - This file
- **`ARCHITECTURE.md`** - Technical architecture and design decisions
- **`PROJECT_SUMMARY.md`** - Development history

## Contributing

To add more chapters:
1. Read the chapter
2. Identify characters and their roles
3. Update `data.js` with character appearances and story entries
4. Test by opening `index.html`

See `ARCHITECTURE.md` for detailed guidance on data format and design principles.

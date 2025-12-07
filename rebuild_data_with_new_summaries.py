import json
import os
import re

# Read all chapter summary .txt files
summaries = {}
for i in range(1, 68):
    filename = f'chapter_data_backup/chapter_summaries/chapter_{i:03d}.txt'
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        # Line 1 is title, line 2 is blank, rest is summary
        title = lines[0].strip()
        # Extract just the chapter title (after "Chapter N: ")
        chapter_title = title.split(': ', 1)[1] if ': ' in title else title
        # Join all lines after the blank line (line 2) and strip trailing newlines
        summary = ''.join(lines[2:]).strip()
        summaries[i] = summary

print(f"Loaded {len(summaries)} chapter summaries from .txt files")

# Read other backup data
with open('chapter_data_backup/capsule_summaries/all_chapters.json', 'r', encoding='utf-8') as f:
    capsules = json.load(f)

with open('chapter_data_backup/chapter_titles.json', 'r', encoding='utf-8') as f:
    titles = json.load(f)

with open('chapter_data_backup/character_stories/all_characters.json', 'r', encoding='utf-8') as f:
    stories = json.load(f)

# Import character data for chapters 13-67
exec(open('character_data_13_67.py', encoding='utf-8').read())

# Build data.js
output = """// Bleak House - Complete Data for All 67 Chapters
// Generated: December 7, 2024
// BACKUP: All data saved in chapter_data_backup/

const BLEAK_HOUSE_DATA = {
    majorCharacters: [
        "Esther Summerson",
        "Lady Dedlock",
        "Sir Leicester Dedlock",
        "Mr. Tulkinghorn",
        "John Jarndyce",
        "Ada Clare",
        "Richard Carstone",
        "Harold Skimpole",
        "Mr. Guppy",
        "Jo",
        "Mr. Bucket",
        "Mr. Snagsby",
        "Miss Flite",
        "Mrs. Jellyby",
        "Caddy Jellyby",
        "Allan Woodcourt",
        "Mr. Vholes",
        "Hortense",
        "Mr. George",
        "Tom Jarndyce"
    ],

    circleOrder: [
        "Bleak House",
        "Chesney Wold",
        "Chancery",
        "London Poor",
        "Legal London",
        "Other"
    ],

    chapterContext: {
"""

# Add capsule summaries
for i in range(1, 68):
    output += f'        {i}: "{capsules[str(i)]}",\n'

output = output.rstrip(',\n') + '\n    },\n\n    chapterTitles: {\n'

# Add titles
for i in range(1, 68):
    output += f'        {i}: "{titles[str(i)]}",\n'

output = output.rstrip(',\n') + '\n    },\n\n'

# Add minimal charactersByChapter (just 1-10 with real data)
output += """    charactersByChapter: {
        1: {
            "Chancery": [
                { name: "Lord High Chancellor", summary: "Presides over Court of Chancery" },
                { name: "Tom Jarndyce", summary: "Deceased litigant who shot himself" }
            ]
        },
        2: {
            "Chesney Wold": [
                { name: "Lady Dedlock", summary: "Reacts mysteriously to handwriting" },
                { name: "Sir Leicester Dedlock", summary: "Her devoted aristocratic husband" },
                { name: "Mrs. Rouncewell", summary: "Housekeeper, tells Ghost Walk legend" }
            ],
            "Legal London": [
                { name: "Mr. Tulkinghorn", summary: "Family lawyer, becomes suspicious" }
            ]
        },
        3: {
            "Bleak House": [
                { name: "Esther Summerson", summary: "Narrator, reveals sad childhood" }
            ]
        },
        4: {
            "Bleak House": [
                { name: "Esther Summerson", summary: "Meets Ada and Richard in London" },
                { name: "Ada Clare", summary: "Beautiful ward in Chancery" },
                { name: "Richard Carstone", summary: "Handsome ward in Chancery" }
            ],
            "Other": [
                { name: "Mrs. Jellyby", summary: "Obsessed with distant philanthropy" },
                { name: "Caddy Jellyby", summary: "Exhausted by mother's schemes" }
            ]
        },
        5: {
            "Bleak House": [
                { name: "Esther Summerson", summary: "Becomes housekeeper" },
                { name: "Ada Clare", summary: "Settles at Bleak House" },
                { name: "Richard Carstone", summary: "Must choose profession" },
                { name: "John Jarndyce", summary: "Kind guardian, creates family atmosphere" },
                { name: "Harold Skimpole", summary: "Charming but parasitic guest" }
            ]
        },
        6: {
            "Bleak House": [
                { name: "Esther Summerson", summary: "Content as housekeeper" },
                { name: "Ada Clare", summary: "Growing close to Richard" },
                { name: "Richard Carstone", summary: "Studying medicine, lacks commitment" },
                { name: "John Jarndyce", summary: "Worried about Richard" },
                { name: "Harold Skimpole", summary: "Parasitic behavior becomes clearer" }
            ]
        },
        7: {
            "Chesney Wold": [
                { name: "Lady Dedlock", summary: "Bored at estate" },
                { name: "Sir Leicester Dedlock", summary: "Devoted to tradition" },
                { name: "Mrs. Rouncewell", summary: "Tells Ghost's Walk legend" }
            ]
        },
        8: {
            "Legal London": [
                { name: "Mr. Tulkinghorn", summary: "Investigates Nemo" },
                { name: "Mr. Snagsby", summary: "Law stationer, helps investigation" },
                { name: "Nemo", summary: "Poor law-writer, mysterious" }
            ],
            "Chancery": [
                { name: "Mr. Krook", summary: "Rag dealer, Nemo's landlord" }
            ]
        },
        9: {
            "Bleak House": [
                { name: "Esther Summerson", summary: "Witnesses charity work" },
                { name: "Ada Clare", summary: "Shows genuine compassion" }
            ],
            "Other": [
                { name: "Mrs. Pardiggle", summary: "Harsh charity worker" }
            ]
        },
        10: {
            "London Poor": [
                { name: "Jo", summary: "Homeless crossing-sweeper, mourns Nemo" },
                { name: "Nemo", summary: "Found dead, pauper burial" }
            ],
            "Legal London": [
                { name: "Mr. Tulkinghorn", summary: "Investigates Nemo's death" },
                { name: "Mr. Snagsby", summary: "At inquest" }
            ],
            "Chesney Wold": [
                { name: "Lady Dedlock", summary: "Visits grave in disguise" }
            ]
        },
        11: {
            "London Poor": [
                { name: "Jo", summary: "Only person mourning Nemo at burial" },
                { name: "Nemo", summary: "Buried in pauper's grave" }
            ],
            "Legal London": [
                { name: "Mr. Snagsby", summary: "Attends funeral, troubled by involvement" },
                { name: "Mrs. Snagsby", summary: "Increasingly jealous and suspicious" }
            ]
        },
        12: {
            "London Poor": [
                { name: "Jo", summary: "Questioned about veiled lady" }
            ],
            "Legal London": [
                { name: "Mr. Tulkinghorn", summary: "Investigating veiled lady" },
                { name: "Mr. Bucket", summary: "Detective hired to investigate" },
                { name: "Mr. Snagsby", summary: "Caught up in investigation" },
                { name: "Mrs. Snagsby", summary: "Jealousy intensifies" }
            ]
        }
    },

    chapterSummaries: {
"""

# Now add the character data for chapters 13-67
for chapter_num in range(13, 68):
    if chapter_num in chapters_13_67:
        output += f"        {chapter_num}: {{\n"
        for circle, chars in chapters_13_67[chapter_num].items():
            output += f'            "{circle}": [\n'
            for char in chars:
                output += f'                {{ name: "{char["name"]}", summary: "{char["summary"]}" }},\n'
            output = output.rstrip(',\n') + '\n            ],\n'
        output = output.rstrip(',\n') + '\n        },\n'

output = output.rstrip(',\n') + '\n    },\n\n    chapterSummaries: {\n'

# Add summaries from the new .txt files
for i in range(1, 68):
    # Replace paragraph breaks with a marker we can split on
    # First escape backslashes and quotes
    escaped_summary = summaries[i].replace('\\', '\\\\').replace('"', '\\"')
    # Replace newlines with space, but preserve paragraph breaks as |||
    paragraphs = escaped_summary.split('\n\n')
    escaped_summary = '|||'.join(p.replace('\n', ' ').strip() for p in paragraphs)
    output += f'        {i}: "{escaped_summary}",\n'

output = output.rstrip(',\n') + '\n    },\n\n    characterStories: {\n'

# Add character stories
for char_name, char_stories in stories.items():
    output += f'        "{char_name}": {{\n'
    for chapter, story in char_stories.items():
        escaped_story = story.replace('\\', '\\\\').replace('"', '\\"')
        output += f'            {chapter}: "{escaped_story}",\n'
    output = output.rstrip(',\n') + '\n        },\n'

output = output.rstrip(',\n') + '\n    }\n};\n'

# Write to data.js
with open('data.js', 'w', encoding='utf-8') as f:
    f.write(output)

print("✓ data.js generated successfully!")
print(f"  File size: {len(output):,} bytes")
print(f"  Chapters: 1-67")
print(f"  Characters with stories: {len(stories)}")

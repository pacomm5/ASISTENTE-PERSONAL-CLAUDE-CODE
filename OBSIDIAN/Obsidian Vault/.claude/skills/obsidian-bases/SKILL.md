---
name: obsidian-bases
description: Create and edit Obsidian Bases (.base files) with views, filters, formulas, and summaries. Use when working with .base files, creating database-like views of notes, or when the user mentions Bases, table views, card views, filters, or formulas in Obsidian.
---

# Obsidian Bases Skill

Create and edit Obsidian Bases (`.base` files) -- YAML-defined database-like views over vault notes.

## Workflow

1. **Create** a `.base` file in the vault
2. **Define scope** with filters to select which notes appear
3. **Add formulas** (optional) for computed properties
4. **Configure views** (table, cards, list, map)
5. **Validate** the YAML syntax

## Schema

```yaml
filters:
  # Global filter: narrows scope for all views
  # Can be a single filter string OR a recursive filter object with and/or/not

formulas:
  property-name: <formula expression>

properties:
  property-name:
    name: Display Name

summaries:
  property-name: <summary formula>

views:
  - type: table | cards | list | map
    name: View Name
    filters: ...       # Optional per-view filter
    order:
      - property: <name>
        direction: asc | desc
    groupBy: <property>
    limit: <number>
    columns:           # Table views only
      - <property-name>
    summaries:         # Table views only
      property-name: <summary formula>
```

## Filter Syntax

Filters narrow down results. They can be applied globally or per-view, and support recursive combinations:

```yaml
# Single filter string
filters: "status == 'active'"

# AND combination
filters:
  and:
    - "status == 'active'"
    - "priority > 2"

# OR combination
filters:
  or:
    - "tags includes 'project'"
    - "tags includes 'work'"

# NOT
filters:
  not: "status == 'archived'"

# Nested
filters:
  and:
    - "status == 'active'"
    - or:
        - "priority >= 3"
        - "due < today()"
```

## Filter Operators

| Operator | Meaning |
|----------|---------|
| `==` | Equal |
| `!=` | Not equal |
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or equal |
| `<=` | Less than or equal |
| `&&` | Logical AND |
| `\|\|` | Logical OR |
| `!` | Logical NOT |
| `includes` | Array contains value |

## Properties

Three types of properties are available:

**Note properties** -- from frontmatter YAML of each note.

**File properties** -- automatically available for all notes:

| Property | Description |
|----------|-------------|
| `file.name` | Note name without extension |
| `file.path` | Full path from vault root |
| `file.mtime` | Last modified date |
| `file.tags` | All tags |
| `file.links` | Outgoing links |

**Formula properties** -- computed values defined in `formulas:`:

```yaml
formulas:
  days-until-due: "duration(due - today()).days"
  is-overdue: "if(due < today(), 'Yes', 'No')"
  full-title: "file.name + ' - ' + status"
```

The `this` keyword refers to the base file itself (or the embedding note when embedded).

## Formula Syntax

Formulas support arithmetic, conditionals, strings, and dates:

```yaml
# Arithmetic
price * quantity

# Conditional
if(status == 'done', 'Complete', 'Pending')

# String concatenation
file.name + " (" + status + ")"

# Date difference (returns a duration object)
due - today()

# Duration to number -- access .days, .hours, or .minutes
duration(due - today()).days

# Nested conditional
if(priority >= 3, if(due < today(), 'Urgent', 'High'), 'Normal')
```

### Key Functions

| Function | Description |
|----------|-------------|
| `date(str)` | Parse a date string |
| `now()` | Current date and time |
| `today()` | Current date (no time) |
| `if(cond, a, b)` | Conditional expression |
| `duration(d)` | Convert to duration object |
| `file(path)` | Reference a file by path |
| `link(path, text)` | Create a link |

## View Types

### Table

```yaml
views:
  - type: table
    name: All Tasks
    columns:
      - file.name
      - status
      - due
      - priority
    order:
      - property: due
        direction: asc
    summaries:
      priority: Average(priority)
```

### Cards

```yaml
views:
  - type: cards
    name: Project Board
    groupBy: status
    order:
      - property: priority
        direction: desc
```

### List

```yaml
views:
  - type: list
    name: Simple List
    order:
      - property: file.mtime
        direction: desc
    limit: 20
```

### Map

Requires coordinate properties and the Maps plugin.

```yaml
views:
  - type: map
    name: Locations
```

## Default Summary Formulas

| Formula | Description |
|---------|-------------|
| `Average(prop)` | Mean value |
| `Min(prop)` | Minimum |
| `Max(prop)` | Maximum |
| `Sum(prop)` | Total |
| `Range(prop)` | Max minus min |
| `Median(prop)` | Median value |
| `Stddev(prop)` | Standard deviation |
| `Earliest(prop)` | Earliest date |
| `Latest(prop)` | Latest date |
| `Checked(prop)` | Count of checked checkboxes |
| `Unchecked(prop)` | Count of unchecked checkboxes |
| `Empty(prop)` | Count of empty values |
| `Filled(prop)` | Count of non-empty values |
| `Unique(prop)` | Count of unique values |

## Complete Examples

### Task Tracker

```yaml
filters: "tags includes 'task'"

formulas:
  days-left: "duration(due - today()).days"
  overdue: "if(due < today() && status != 'done', true, false)"

properties:
  days-left:
    name: Days Left

views:
  - type: table
    name: Active Tasks
    filters: "status != 'done'"
    columns:
      - file.name
      - status
      - priority
      - due
      - days-left
    order:
      - property: due
        direction: asc
    summaries:
      file.name: Filled(file.name)

  - type: cards
    name: By Priority
    filters: "status != 'done'"
    groupBy: priority
    order:
      - property: days-left
        direction: asc
```

### Reading List

```yaml
filters: "tags includes 'book'"

formulas:
  status-icon: "if(status == 'read', 'Done', if(status == 'reading', 'In progress', 'To read'))"

views:
  - type: table
    name: All Books
    columns:
      - file.name
      - author
      - status-icon
      - rating
      - file.mtime
    order:
      - property: file.mtime
        direction: desc
```

### Daily Notes Index

```yaml
filters: "file.path matches '^\\d{4}-\\d{2}-\\d{2}\\.md$'"

views:
  - type: list
    name: Recent Days
    order:
      - property: file.name
        direction: desc
    limit: 30
```

## YAML Quoting Rules

Quote strings that contain special characters (`==`, `!=`, `<`, `>`, `:`, `#`):

```yaml
# Correct
filters: "status == 'active'"
formulas:
  label: "if(priority > 2, 'High', 'Low')"

# Incorrect -- will cause YAML parse error
filters: status == active
```

## Troubleshooting

- **No results**: Check filter syntax and ensure frontmatter properties exist in the target notes.
- **Formula error**: Verify property names match exactly (case-sensitive). Duration arithmetic requires `.days`/`.hours`/`.minutes` to extract numbers.
- **View not showing**: Confirm `type` is one of `table`, `cards`, `list`, `map`.

## References

- [Obsidian Bases documentation](https://help.obsidian.md/bases)

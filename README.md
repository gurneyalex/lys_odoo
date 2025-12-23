# Lys History

Custom Odoo 19.0 module set for managing historical data (people, locations, colors, clothing, and purchases).

## Environment

- Python 3.12
- Odoo 19.0 installed in a virtualenv
- Custom addons in `src/odoo/addons`

Activate the virtual environment and use the local Python:

```sh
source .venv/bin/activate
# or prefix commands with .venv/bin/...
```

## Running Odoo

From the project root:

```sh
.venv/bin/odoo -c odoo.cfg
```

The `odoo.cfg` file defines:

- database connection
- `addons_path` including `src/odoo/addons` and the Odoo community addons

## Tests

Run the test suite with:

```sh
.venv/bin/pytest --odoo-config=odoo.cfg --odoo-database=lys_test
```

## Development Notes

- Target Odoo version: **19.0**
- Use `<list>` views (not `<tree>`) and use `list` in view names/xmlids
- All user‑visible strings in Python and XML must be in **US English**
- Translations are managed via gettext files in `i18n/` (for example `i18n/fr.po`)
- Run `pre-commit` on changed files, for example:

```sh
pre-commit run path/to/file.py
```

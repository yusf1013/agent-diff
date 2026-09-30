import sys, json, importlib
sys.path.insert(0, 'backend')
out = {}
for svc in ['slack', 'box', 'linear']:
    mod = importlib.import_module(f'src.services.{svc}.database.schema')
    base = getattr(mod, 'Base', None)
    md = base.metadata
    tables = {}
    for t in md.sorted_tables:
        uniq = []
        for c in t.constraints:
            cname = type(c).__name__
            cols = [col.name for col in getattr(c, 'columns', [])]
            if cname in ('UniqueConstraint', 'PrimaryKeyConstraint'):
                uniq.append({'kind': cname, 'columns': cols})
        for col in t.columns:
            if col.unique:
                uniq.append({'kind': 'unique_column', 'columns': [col.name]})
        for ix in t.indexes:
            if ix.unique:
                uniq.append({'kind': 'unique_index', 'columns': [c.name for c in ix.columns]})
        fks = [{'column': fk.parent.name, 'ref_table': fk.column.table.name, 'ref_column': fk.column.name,
                'ondelete': fk.ondelete} for fk in t.foreign_keys]
        tables[t.name] = {'unique': uniq, 'fks': fks, 'columns': [c.name for c in t.columns]}
    out[svc] = tables
json.dump(out, open(sys.argv[1], 'w'), indent=1)
for svc, tables in out.items():
    print('==', svc, len(tables), 'tables')
    for name, t in tables.items():
        u = [('+'.join(x['columns'])) for x in t['unique'] if x['kind'] != 'PrimaryKeyConstraint']
        pk = [('+'.join(x['columns'])) for x in t['unique'] if x['kind'] == 'PrimaryKeyConstraint']
        print(f"  {name}: pk={pk} unique={u} fks={[(f['column'], f['ref_table']) for f in t['fks']]}")

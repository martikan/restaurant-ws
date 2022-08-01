gen_req:
	rm requirements.txt && python -m pip freeze > requirements.txt

add_migration:
ifdef name
	alembic revision -m ${name}
else
	@echo '"name" is not defined. Please add a name for the migration.'
endif

migrateup:
	alembic upgrade head

migrateup1:
	alembic upgrade +1

migratedown:
ifdef rev
	alembic downgrade ${rev}
else
	alembic downgrade base
endif

migratedown1:
	alembic downgrade -1

start-dev:
	uvicorn main:app --reload

start:
	export PROFILE=prod && uvicorn main:app

.PHONY: gen_req add_migration migrateup start-dev start
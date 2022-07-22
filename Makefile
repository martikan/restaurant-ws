postgres:
	docker run --name postgres13 -p 5432:5432 -e POSTGRES_USER=restaurant -e POSTGRES_PASSWORD=aaa -d postgres:13

createdb:
	docker exec -it postgres13 createdb --username=restaurant --owner=restaurant restaurant

dropdb:
	docker exec -it postgres13 dropdb restaurant

start-dev:
	@$(MAKE) -C api start-dev
start:
	@$(MAKE) -C api start

.PHONY: postgres createdb dropdb start-dev start
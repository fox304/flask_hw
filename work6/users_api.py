import pandas as pd

from hw.work6.main import *

@app.post("/")
async def create_user(user: Users):
	query = users.insert().values(**user.__dict__)
	await database.execute(query)


@app.get("/users/", response_class=HTMLResponse)
async def get_users(request: Request):
	query = users.select()
	our_table = pd.DataFrame( user for user in await database.fetch_all(query)).to_html()
	return templates.TemplateResponse("users.html", {"request": request, "user_table": our_table})


@app.get("/user/{num}", response_model=Users)
async def get_user(num: int):
	query = users.select().where(users.c.id == num)
	our_table = pd.DataFrame( user for user in await database.fetch_all(query)).to_html()
	return await database.fetch_one(query)


@app.put("/user/{num}", response_model=Users)
async def update_user(num: int, new_user: Users):
	query = users.update().where(users.c.id == num).values(**new_user.__dict__)
	await database.execute(query)
	return {**new_user.__dict__}


@app.delete("/user/{num}")
async def delete_user(num: int):
	query = users.delete().where(users.c.id == num)
	await database.execute(query)
	return {'message': f'User {num} deleted'}

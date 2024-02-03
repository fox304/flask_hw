# from hw.work6.main import *
from main import *

@app.post("/")
async def create_orders(product: Orders):
	query = orders.insert().values(**product.__dict__)
	await database.execute(query)


@app.get("/orders/", response_class=HTMLResponse)
async def get_orders(request: Request):
	query = orders.select()
	our_table = pd.DataFrame(order for order in await database.fetch_all(query)).to_html()
	return templates.TemplateResponse("orders.html", {"request": request, "orders_table": our_table})


@app.get("/order/{num}", response_model=Orders)
async def get_order(num: int):
	query = orders.select().where(orders.c.id == num)
	pd.DataFrame(order for order in await database.fetch_all(query)).to_html()
	return await database.fetch_one(query)


@app.put("/order/{num}", response_model=Orders)
async def update_order(num: int, new_order: Orders):
	query = orders.update().where(orders.c.id == num).values(**new_order.__dict__)
	await database.execute(query)
	return {**new_order.__dict__}


@app.delete("/order/{num}")
async def delete_order(num: int):
	query = orders.delete().where(orders.c.id == num)
	await database.execute(query)
	return {'message': f'Order {num} deleted'}

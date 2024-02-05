# from hw.work6.main import *
from main import *


@app.post("/")
async def create_product(product: Goods):
	query = goods.insert().values(**product.__dict__)
	await database.execute(query)


@app.get("/goods/", response_class=HTMLResponse)
async def get_products(request: Request):
	query = goods.select()
	our_table = pd.DataFrame(product for product in await database.fetch_all(query)).to_html()
	return templates.TemplateResponse("goods.html", {"request": request, "goods_table": our_table})


@app.get("/product/{num}", response_model=Goods)
async def get_product(num: int):
	query = goods.select().where(goods.c.id == num)
	pd.DataFrame(product for product in await database.fetch_all(query)).to_html()
	return await database.fetch_one(query)


@app.put("/product/{num}", response_model=Goods)
async def update_product(num: int, new_product: Goods):
	query = goods.update().where(goods.c.id == num).values(**new_product.__dict__)
	await database.execute(query)
	return {**new_product.__dict__}


@app.delete("/product/{num}")
async def delete_product(num: int):
	query = goods.delete().where(goods.c.id == num)
	await database.execute(query)
	return {'message': f'Product {num} deleted'}

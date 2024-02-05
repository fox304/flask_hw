"""
Урок 6. Дополнительные возможности FastAPI

Необходимо создать базу данных для интернет-магазина.
База данных должна состоять из трёх таблиц: товары, заказы и пользователи.
— Таблица «Товары» должна содержать информацию о доступных товарах, их описаниях и ценах.
— Таблица «Заказы» должна содержать информацию о заказах, сделанных пользователями.
— Таблица «Пользователи» должна содержать информацию о зарегистрированных пользователях магазина.
• Таблица пользователей должна содержать следующие поля: id (PRIMARY KEY), имя, фамилия, адрес электронной почты и пароль.
• Таблица заказов должна содержать следующие поля: id (PRIMARY KEY), id пользователя (FOREIGN KEY), id товара (FOREIGN KEY), дата заказа и статус заказа.
• Таблица товаров должна содержать следующие поля: id (PRIMARY KEY), название, описание и цена.

Создайте модели pydantic для получения новых данных и возврата существующих в БД для каждой из трёх таблиц (итого шесть моделей).
Реализуйте CRUD операции для каждой из таблиц через создание маршрутов, REST API (итого 15 маршрутов).
* Чтение всех
* Чтение одного
* Запись
* Изменение
* Удаление

"""
import databases
import sqlalchemy
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field
from datetime import date
import pandas as pd

DATABASE_URL = "sqlite:///mydatabase.db"
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table("Пользователи",
			 metadata,
			 sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
			 sqlalchemy.Column("first_name", sqlalchemy.String(10)),
			 sqlalchemy.Column("second_name", sqlalchemy.String(10)),
			 sqlalchemy.Column("email", sqlalchemy.String(32)),
			 sqlalchemy.Column("password", sqlalchemy.String(128)),
			 )

goods = sqlalchemy.Table("Товары",
			 metadata,
			 sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
			 sqlalchemy.Column("name", sqlalchemy.Integer),
			 sqlalchemy.Column("description", sqlalchemy.String(200)),
			 sqlalchemy.Column("price", sqlalchemy.String(500)),
			 )

orders = sqlalchemy.Table("Заказы",
			  metadata,
			  sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
			  sqlalchemy.Column("id_user", sqlalchemy.ForeignKey('Пользователи.id')),
			  sqlalchemy.Column("id_good", sqlalchemy.ForeignKey('Товары.id')),
			  sqlalchemy.Column("status", sqlalchemy.String(32)),
			  sqlalchemy.Column("date", sqlalchemy.String(128)),
			  )

engine = sqlalchemy.create_engine(DATABASE_URL,
				  connect_args={"check_same_thread": False})
metadata.create_all(engine)

app = FastAPI()
templates = Jinja2Templates(directory="templates")


class Users(BaseModel):
	first_name: str = Field(max_length=10)
	second_name: str = Field(max_length=20)
	email: str = Field(max_length=20)
	password: str = Field(max_length=20, min_length=4)


class Goods(BaseModel):
	name: str = Field(max_length=10)
	description: str = Field(title="Описание товара: ", max_length=200)
	price: int = Field(lt=500, gt=10)


class Orders(BaseModel):
	id_user: int = Field(ge=1)
	id_good: int = Field(ge=1)
	status: bool = Field(default_factory=False)
	date: date

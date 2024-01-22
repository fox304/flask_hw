"""
Написать программу, которая скачивает изображения с заданных URL-адресов
и сохраняет их на диск. Каждое изображение должно сохраняться в отдельном файле,
название которого соответствует названию изображения в URL-адресе.
Например, URL-адрес: https://example/images/image1.jpg -> файл на диске: image1.jpg
— Программа должна использовать многопоточный, многопроцессорный и асинхронный подходы.
— Программа должна иметь возможность задавать список URL-адресов через аргументы командной строки.
— Программа должна выводить в консоль информацию о времени скачивания каждого изображения
  и общем времени выполнения программы.
"""
import asyncio
import multiprocessing
import os.path
import threading
import time

import aiohttp
import requests

urls = [
	'https://vplate.ru/images/article/orig/2020/03/idei-dlya-novogodnih-vecherinok.jpg',
	'https://klike.net/uploads/posts/2023-04/1681274108_3-70.jpg',
	'https://photo-hair.ru/wp-content/uploads/2021/09/4-30.jpg',
	'http://s2.fotokto.ru/photo/full/224/2245472.jpg',
	'https://ohotaportal.ru/wp-content/uploads/1/9/3/19365636e60b48de386d64c9b24e512d.jpeg'

]


def decorator_(func):
	def wrap():
		for url in urls:
			func(url)
	return wrap


def decorator_for_async(func):
	async def wrap():
		list_ = [asyncio.ensure_future(func(url)) for url in urls]
		await asyncio.gather(*list_)
	return wrap


def function(url):
	name = 'images' + '/' + url.split('/')[-1]
	with open(name, 'wb') as f:
		f.write(requests.get(url).content)


@decorator_
def sync_(url):
	function(url)


@decorator_
def thread_(arg):
	t = threading.Thread(target=function, args=(arg,))
	t.start()


@decorator_
def proc_(arg):
	p = multiprocessing.Process(target=function, args=(arg,))
	p.start()


@decorator_for_async
async def async_(url):
	async with aiohttp.ClientSession() as session:
		async with session.get(url) as response:
			name = 'images' + '/' + url.split('/')[-1]
			text = await response.content.read()
			with open(name, 'wb') as f:
				f.write(text)




if __name__ == '__main__':
	if not os.path.exists('images'):
		os.mkdir('images')

	start = time.time()
	sync_()
	print(time.time() - start)

	start = time.time()
	thread_()
	print(time.time() - start)

	start = time.time()
	proc_()
	print(time.time() - start)

	start = time.time()

	loop = asyncio.get_event_loop()
	loop.run_until_complete(async_())

	print(time.time() - start)

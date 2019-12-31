from newscontent.wsgi import *
from news.models import Column,Article

def main():
	columns_urls=[("体育","sports"),("社会","society"),
	("科技","tech"),("军事","military"),("娱乐","entertainment"),
	("财经","economics"),("教育","education"),("国际","international"),]
	for column_name,url in columns_urls:
		c=Column.objects.get_or_create(name=column_name,slug=url)[0]
		#创建10片新闻
		for i in range(1,11):
			article=Article.objects.get_or_create(title="{}新闻_{}".format(
				column_name,i),slug="article_{}".format(i),
			content="新闻详细内容：{} {}".format(column_name,i))[0]
			article.column.add(c)

if __name__ == '__main__':
	main()
	print("Done!")

# from itemadapter import ItemAdapter


# class ZimraNoticesPipeline:
#     def process_item(self, item, spider):
#         return item

from scrapy.pipelines.files import  FilesPipeline

class CustomFilePipelines(FilesPipeline):
    def file_path(self, request, response=None, info=None, *, item=None):
        return item.get('title')+'.pdf'
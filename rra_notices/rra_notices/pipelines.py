import re
from itemadapter import ItemAdapter

   
class CleanPipeLineRRA:
    def process_item(self, item,spider): 
        if spider.name == 'rra_spider':
            # Use re.search to apply the regular expression on 'notice_date'
            date_match = re.search(r'(\d{2}\.\d{2}\.\d{4})', item['notice_date']) 
            # If the regular expression matches, set 'notice_date' to the matched value, otherwise set it to None
            item['notice_date'] = date_match.group(1) if date_match else None  
        
        return item
        
        

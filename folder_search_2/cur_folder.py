'''
Created on Jun 12, 2020

@author: Sumit
'''
class cur():
    path=""
    folder_list=[]
    
    def __init__(self,path,folder_list):
        self.path=path
        self.folder_list=folder_list
        
    def get_path(self):
        return self.path
    
    def get_folder_list(self):
        return self.folder_list
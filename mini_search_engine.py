def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1:
        return None,0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"',start_quote+1)
    url = page[start_quote+1:end_quote]
    return url,end_quote


url,endpos = get_next_target('NOT "GOOD" at all!')

if url:
    print ("Here!")

else:
    print ("Not here!")






    

    





def get_all_links(page):
    links = []
    while True:
        url,endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]

        else:
            break

        return links

    



    




    
    




        






    
            
                
        


def crawl_web(seed):
    to_crawl = [seed]
    crawled = []
    index = {}
    graph = {}
    while tocrawl :
        page = tocrawl.pop()
        if page not in crawled:
            content = get_page(page)
            add_page_to_index(index,page,content)
            out_links = get_all_links(content)
            graph[page] = outlinks
            union(to_crawl,out_links)
            crawled.append(page)

        return index,graph

index,graph = crawl_web('............')
print graph['..]
print ranks




            



def compute_ranks(graph):
    d= 0.8 #damping factor
    numloops = 10

    ranks = {}
    npages = len(graph)
    for page in graph :
        ranks[page] = 1.0 / npages


        for i in range(0,numloops):
            newranks = {}
            for page in graph:
                newrank = (1-d)/npages
            for node in graph:
                if page in graph[node]:
            newrank = newrank+d*(rank[node]/len(graph[node]))
            
            

                  
       newranks[page] = newrank
       ranks = newranks
       return ranks






    


def union(a,b):
    for e in b:
        if e not in a:
            a.append(e)





            



def add_page_to_index(index,url,content):
    words = content.split()
    for word in words:
        add_to_index(index,word,url)






def add_to_index(index,keyword,url):
    if keyword in index:
        index[keyword].append(url)
        else:
            index[keyword]=[url]



def lookup(index,keyword):
       if keyword in index :
           return index[keyword]
        else:
            return None

    

    
        
        
    
    




            

             

                
         

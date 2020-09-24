def get_index_of_bracket(text):
    start = text.find("{")
    end = text.rfind("}")
    return start,end

def format_bib(path):
    """
    args:
        path:"txt file of bib"
    """
    with open(path,"a") as f:
        f.write("@")

        
    template = "- {0},**{1}**,{2} {3} [[Paper]]({4})"

    f = open(path,'r')
    
    text = f.readlines()

    bib_list = []
    for idx,item in enumerate(text):
        if "@" in item:
            temp = idx 
            bib_list.append(idx)
    bib_text_list = []
    

    for i in range(bib_list.__len__()-1):
        temp = []
        temp.append([item for item in text[bib_list[i]:bib_list[i+1]]])
        bib_text_list.append(temp)

    
    result = []
    for item in bib_text_list:
        url = ""
        for i in item[0]:
            
            if "title" in i and "book" not in i:
                start,end = get_index_of_bracket(i)
                title = i[start+1:end]
            elif "author" in i:
                start,end = get_index_of_bracket(i)
                author = i[start+1:end]
            elif "booktitle" in i or "journal" in i:
                start,end = get_index_of_bracket(i)
                journal = i[start+1:end]
            elif "year" in i:
                start,end = get_index_of_bracket(i)
                year = i[start+1:end]
            
            elif "url" in i:
                start,end = get_index_of_bracket(i)
                url = i[start+1:end]
                
        result.append(template.format(author,title,journal,year,url))
    return result


if __name__ == "__main__":
    print(format_bib("bib.txt"))
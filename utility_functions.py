from typing import List

def split_string(table_string: str) -> List[str]:
    n = 1994
    if len(table_string) > n:
        chunks = []
        i = 0
        while True:
            if len(table_string) - i < n:
                chunk = table_string[i:len(table_string)]
                chunks.append(chunk)
                break
            else:
                newline_position = table_string.rfind("\n", i, i+n)            
                newline_position = newline_position+1
                chunk = table_string[i:newline_position]
                i = newline_position
                chunks.append(chunk)
        
        return chunks
    else:
        return [table_string]

def convert_string_to_codeblock_string(string_to_format: str) -> str:
    return f"```{string_to_format}```"
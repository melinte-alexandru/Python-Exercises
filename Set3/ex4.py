# 4. XML element
def build_xml_element(tag, content, **kwargs):
    attrs = " ".join([f'{k}="{v}"' for k, v in kwargs.items()])
    return f"<{tag} {attrs}>{content}</{tag}>"
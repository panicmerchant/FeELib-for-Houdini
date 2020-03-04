
import hou

def buildAttribMenu(node, input_num=0, attribClass='point', attribType='all'):
    try:
        input = node.inputs()[input_num]
        geo = input.geometry()
        if attribClass=='point':
            allattrib = geo.pointAttribs()
        elif attribClass=='prim':
            allattrib = geo.primAttribs()
        elif attribClass=='vertex':
            allattrib = geo.vertexAttribs()
        else:
            allattrib = geo.globalAttribs()
        menu = []
        for attrib in allattrib:
            if attribType=='int':
                if attrib.dataType()!=hou.attribData.Int:
                    continue
            elif attribType=='float':
                if attrib.dataType()!=hou.attribData.Float:
                    continue
            elif attribType=='string':
                if attrib.dataType()!=hou.attribData.String:
                    continue
            menu += [attrib.name()]
            menu += [attrib.name()]
    except:
        return []
    
    return menu

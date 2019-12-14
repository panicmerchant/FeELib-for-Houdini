# script name: OPmenu
# create date:2018-11-10
#	   E-mail:junvfx@foxmail.com

import hou

toolname = kwargs["toolname"].split(".")[-1]

if toolname == "old_version":
	nodeType = kwargs["node"].type().name()
	if ":" in nodeType:
		#plane = hou.ui.paneTabOfType(hou.paneTabType.NetworkEditor)
		#pos = plane.selectPosition()
		#node = plane.currentNode()
		pos = kwargs["node"].position() - hou.Vector2(-2,0.5)
		nodePath = kwargs["node"].path()
		hou.node( nodePath[:nodePath.rfind("/")] ).createNode( nodeType[:nodeType.find(":")], exact_type_name=True).setPosition(pos)


elif toolname == "out":
	node = kwargs["node"]
	#plane mouse position to node
	#plane = hou.ui.paneTabOfType(hou.paneTabType.NetworkEditor)
	#pos = plane.selectPosition()
	pos = node.position() - hou.Vector2(0,1.5)
	nullnode = hou.node(node.parent().path()).createNode("null", "OUT_%s"%node.name())
	nullnode.setInput(0,node)
	nullnode.setPosition(pos)

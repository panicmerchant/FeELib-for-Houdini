# -*- coding: utf-8 -*-
# script name: PARMmenu
# create date:2018-11-10
#	   E-mail:junvfx@foxmail.com

import hou
import os
import subprocess

toolname = kwargs["toolname"].split(".")[-1]
parms = kwargs["parms"]

if toolname == "window_folder":
	path = parms[0].eval()
	try:
		if os.path.exists(path[:path.rfind("/")]):
			subprocess.call('start explorer %s'%path[:path.rfind("/")].replace("/","\\"), shell = True)
	except:
		pass

else:
	must_node = ["centroid", "BBOX_MIN", "BBOX_MAX", "BBOX_SIZE", "point", "detail", "prim1", "primuv"]
	X=""
	Y=""
	Z=""
	result = 0
	if toolname in must_node:
		result = hou.ui.displayMessage("选择关联节点来源", buttons =("上游节点","手动选择","取消"), severity=hou.severityType.Message)
		if result != 2:
			path = ""
			if result == 0:
				path = '''opinputpath(".",0)'''
			if result == 1:
				current_node = hou.ui.selectNode( initial_node= parms[0].node() )
				temp =  parms[0].node().relativePathTo( hou.node(current_node) )
				path = '''"%s"'''%temp
			if toolname == "centroid":
				X = '''centroid(%s,D_X)'''%path
				Y = '''centroid(%s,D_Y)'''%path
				Z = '''centroid(%s,D_Z)'''%path

			elif toolname == "BBOX_MIN":
				X = '''bbox(%s,D_XMIN)'''%path
				Y = '''bbox(%s,D_YMIN)'''%path
				Z = '''bbox(%s,D_ZMIN)'''%path

			elif toolname == "BBOX_MAX":
				X = '''bbox(%s,D_XMAX)'''%path
				Y = '''bbox(%s,D_YMAX)'''%path
				Z = '''bbox(%s,D_ZMAX)'''%path

			elif toolname == "BBOX_SIZE":
				X = '''bbox(%s,D_XSIZE)'''%path
				Y = '''bbox(%s,D_YSIZE)'''%path
				Z = '''bbox(%s,D_ZSIZE)'''%path

			elif toolname == "point":
				X = '''point(%s,0,"P",0)'''%path
				Y = '''point(%s,0,"P",1)'''%path
				Z = '''point(%s,0,"P",2)'''%path

			elif toolname == "detail":
				X = '''detail(%s,"attr_name",0)'''%path
				Y = '''detail(%s,"attr_name",1)'''%path
				Z = '''detail(%s,"attr_name",2)'''%path

			elif toolname == "prim1":
				X = '''prim(%s,0,"P",0)'''%path
				Y = '''prim(%s,0,"P",1)'''%path
				Z = '''prim(%s,0,"P",2)'''%path

			elif toolname == "primuv":
				X = '''primuv(%s,0,"P",0,@u.x,@u.y)'''%path
				Y = '''primuv(%s,0,"P",1,@u.x,@u.y)'''%path
				Z = '''primuv(%s,0,"P",2,@u.x,@u.y)'''%path

	else:
		if toolname == "CEX1":
			X = '''$CEX'''
			Y = '''$CEY'''
			Z = '''$CEZ'''

		elif toolname == "CEX2":
			X = '''-$CEX'''
			Y = '''-$CEY'''
			Z = '''-$CEZ'''

		elif toolname == "fit1":
			X = '''fit($FF,0,10,1,5)'''
			Y = '''fit($FF,0,10,1,5)'''
			Z = '''fit($FF,0,10,1,5)'''

		elif toolname == "fit01":
			X = '''fit01(rand($PT),1,5)'''
			Y = '''fit01(rand($PT),1,5)'''
			Z = '''fit01(rand($PT),1,5)'''

		elif toolname == "vtorigin":
			X = '''vtorigin("",chsop("/obj/geo"))[0]'''
			Y = '''vtorigin("",chsop("/obj/geo"))[1]'''
			Z = '''vtorigin("",chsop("/obj/geo"))[2]'''

		elif toolname == "vrorigin":
			X = '''vrorigin("",chsop("/obj/geo"))[0]'''
			Y = '''vrorigin("",chsop("/obj/geo"))[1]'''
			Z = '''vrorigin("",chsop("/obj/geo"))[2]'''

		elif toolname == "opdigits":
			X = '''opdigits(opname("."))'''
			Y = '''opdigits(opname("."))'''
			Z = '''opdigits(opname("."))'''

	if result != 2:
		for i,parm in enumerate(parms):
			if i == 0:
				parms[i].setExpression( X )

			if i == 1:
				parms[i].setExpression( Y )

			if i == 2:
				parms[i].setExpression( Z )
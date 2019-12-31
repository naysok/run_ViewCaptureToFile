import Rhino
import rhinoscriptsyntax as rs
import scriptcontext as sc
import ghpythonlib.components as ghpc



def brep_list_from_guid_list(brep_list):
    bl = []
    
    for i in xrange(len(brep_list)):
        bl.append(rs.coercebrep(brep_list[i]))
    
    return bl


breps = brep_list_from_guid_list(INSERT)
# print(breps)



#################################

### (1) String on Python
#p = "C:\\Users\\yoshioca\\Documents\\run_ViewCaptureToFile\\out_python.png"
p = r"C:\Users\yoshioca\Documents\run_ViewCaptureToFile\out_python.png"

_path_ = p



### (2) Panel >> ghPython(ghdoc)
#_path_ = PATH_ghdoc


### (3) Panel >> ghPython()
#_path_ = PATH_str

#################################



sc.doc = ghdoc

if BOOL:
    
    sc.doc = Rhino.RhinoDoc.ActiveDoc
    for i in xrange(len(breps)):
        b = breps[i]
        print(b)
        sc.doc.Objects.AddBrep(b)
    
    
    query = "-ViewCaptureToFile "+ \
        " W=1080 H=1080 S=1 L=_No D=_No R=_No A=_No T=_No " + \
        _path_ + \
        " _Enter " + \
        " _SelAll _Delete"
        
    rs.Command(query)
    
    print(query)


sc.doc = ghdoc

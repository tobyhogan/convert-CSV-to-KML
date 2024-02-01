import csv

# write the input file inside quotes
in_file = str( "test.csv" )
print( "input file is " + str(in_file) )

# read data
data = csv.reader( open(in_file), delimiter = ',' )

# open the output file
f = open( in_file[:-4] + '.kml', 'w')

# writing the kml file
f.write("<?xml version='1.0' encoding='UTF-8'?>\n")
f.write("<kml xmlns='http://earth.google.com/kml/2.1'>\n")
f.write("<Folder>\n")
f.write("   <name>" + in_file[:-4] + "</name>\n")

#	<Placemark>
#		<name>ALBE</name>
#		<description><![CDATA[ALBE/Alberta Beach Family RV Park   CP PH:780.924.2333 mid may-late sep  SITES:30  #AMEN:WES approx  mi  of Alberta Beach  53.675 -114.353]]></description>
#		<Point>
#			<altitudeMode>clampToGround</altitudeMode>
#			<coordinates>-114.353,53.675,0</coordinates>
#		</Point>
#	</Placemark>

for row in data:
    f.write("   <Placemark>\n")
    s = str(row[2])
    f.write("       <name>" + s[0:4] + "</name>\n")
    f.write("       <description><![CDATA[" + str(row[2]) + "]]></description>\n")
    f.write("       <Point>\n")
    f.write("           <altitudeMode>clampToGround</altitudeMode>\n")
    f.write("           <coordinates>" + str(row[0]) + "," + str(row[1]) + ",0</coordinates>\n")
    f.write("       </Point>\n")
    f.write("   </Placemark>\n")
    
f.write("</Folder>\n")
f.write("</kml>\n")

f.close()

print ( str(in_file[:-4] ) + ".kml created")

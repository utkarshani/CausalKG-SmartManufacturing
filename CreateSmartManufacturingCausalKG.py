import rdflib
from rdflib import Dataset
from rdflib import URIRef
from rdflib.namespace import Namespace, NamespaceManager
from rdflib.namespace import RDF, RDFS
from rdflib import Graph
import uuid
import pandas as pd
import numpy as np

print("Running Code")
# Define namespaces
smartManufacturing = Namespace("http://purl.org/net/SmartManufacturing/v00/")
smartManufacturingData = Namespace("http://purl.org/net/SmartManufacturing/v00/data/")
causal = Namespace("http://semantic.bosch.com/causal/v00/")
scene = Namespace("http://semantic.bosch.com/scene/v02/")
sosa = Namespace("http://www.w3.org/ns/sosa/")
cora = Namespace("http://purl.org/ieee1872-owl/cora-bare#")
dul = Namespace("http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#")
om = Namespace("http://www.ontology-of-units-of-measure.org/resource/om-2/")
rparts = Namespace("http://purl.org/ieee1872-owl/rParts/")
owl = Namespace("http://www.w3.org/2002/07/owl#")

g = Graph()
namespace_manager = NamespaceManager(Graph())
namespace_manager.bind('', smartManufacturingData, override=False)
namespace_manager.bind("smartManufacturing", smartManufacturing, override=True)
namespace_manager.bind("causal", causal, override=True)
namespace_manager.bind("scene", scene, override=True)
namespace_manager.bind("sosa", sosa, override=True)
namespace_manager.bind("cora", cora, override=True)
namespace_manager.bind("dul", dul, override=True)
namespace_manager.bind("om", om, override=True)
namespace_manager.bind("rparts", rparts, override=True)
namespace_manager.bind("owl", owl, override=True)
g.namespace_manager = namespace_manager

g.add((smartManufacturing.SafetyDoor, RDFS.subClassOf, sosa.Sensor))

safetyDoor1 = URIRef(smartManufacturingData+str(uuid.uuid4()))
safetyDoor2 = URIRef(smartManufacturingData+str(uuid.uuid4()))

g.add((safetyDoor1, RDF.type, smartManufacturing.SafetyDoor))
g.add((safetyDoor2, RDF.type, smartManufacturing.SafetyDoor))

g.add((smartManufacturing.HMIEStopButton,RDFS.subClassOf, sosa.Sensor))

HMIEStopButton = URIRef(smartManufacturingData+str(uuid.uuid4()))
g.add((HMIEStopButton, RDF.type, smartManufacturing.HMIEStopButton))

g.add((smartManufacturing.Angle, RDFS.subClassOf, sosa.ObservableProperty))
angle = URIRef(smartManufacturingData+str(uuid.uuid4()))

g.add((angle, RDF.type, smartManufacturing.Angle))
g.add((angle, om.hasUnit, om.AngleUnit))

robot1 = URIRef(smartManufacturingData+str(uuid.uuid4()))
robot2 = URIRef(smartManufacturingData+str(uuid.uuid4()))
robot3 = URIRef(smartManufacturingData+str(uuid.uuid4()))
robot4 = URIRef(smartManufacturingData+str(uuid.uuid4()))

g.add((robot1, RDF.type, cora.Robot))
g.add((robot2, RDF.type, cora.Robot))
g.add((robot3, RDF.type, cora.Robot))
g.add((robot4, RDF.type, cora.Robot))

g.add((smartManufacturing.GripperPotentiometerSensor, RDFS.subClassOf, sosa.Sensor))
g.add((smartManufacturing.GripperLoadSensor, RDFS.subClassOf, sosa.Sensor))

potentiometer1 = URIRef(smartManufacturingData+str(uuid.uuid4()))
g.add((potentiometer1, RDF.type, smartManufacturing.GripperPotentiometerSensor))
g.add((robot1, rparts.robotSensingPart, potentiometer1))

potentiometer2 = URIRef(smartManufacturingData+str(uuid.uuid4()))
load2 = URIRef(smartManufacturingData+str(uuid.uuid4()))
g.add((potentiometer2, RDF.type, smartManufacturing.GripperPotentiometerSensor))
g.add((load2, RDF.type, smartManufacturing.GripperLoadSensor))
g.add((robot2, rparts.robotSensingPart, potentiometer2))
g.add((robot2, rparts.robotSensingPart, load2))

potentiometer3 = URIRef(smartManufacturingData+str(uuid.uuid4()))
load3 = URIRef(smartManufacturingData+str(uuid.uuid4()))
g.add((potentiometer3, RDF.type, smartManufacturing.GripperPotentiometerSensor))
g.add((load3, RDF.type, smartManufacturing.GripperLoadSensor))
g.add((robot3, rparts.robotSensingPart, potentiometer3))
g.add((robot3, rparts.robotSensingPart, load3))

potentiometer4 = URIRef(smartManufacturingData+str(uuid.uuid4()))
g.add((potentiometer4, RDF.type, smartManufacturing.GripperPotentiometerSensor))
g.add((robot4, rparts.robotSensingPart, potentiometer4))

robotSJoint2 = URIRef(smartManufacturingData+str(uuid.uuid4()))
g.add((robotSJoint2, RDF.type, smartManufacturing.RobotSJoint))
g.add((robot2, cora.robotPart, robotSJoint2))

robotSJoint3 = URIRef(smartManufacturingData+str(uuid.uuid4()))
g.add((robotSJoint3, RDF.type, smartManufacturing.RobotSJoint))
g.add((robot3, cora.robotPart, robotSJoint3))

g.add((smartManufacturing.NoNose, RDFS.subClassOf, smartManufacturing.Anamoly))
g.add((smartManufacturing.NoBody1, RDFS.subClassOf, smartManufacturing.Anamoly))
g.add((smartManufacturing.NoBody2, RDFS.subClassOf, smartManufacturing.Anamoly))
g.add((smartManufacturing.NoNoseNoBody2, RDFS.subClassOf, smartManufacturing.Anamoly))
g.add((smartManufacturing.NoNoseNoBody2NoBody1, RDFS.subClassOf, smartManufacturing.Anamoly))

g.add((smartManufacturing.Anamoly, RDFS.subClassOf, dul.Event))

g.add((smartManufacturing.Closed, RDFS.subClassOf, dul.Event))
g.add((smartManufacturing.Open, RDFS.subClassOf, dul.Event))
g.add((smartManufacturing.OpenWithPart, RDFS.subClassOf, dul.Event))
g.add((smartManufacturing.ClosedWithPart, RDFS.subClassOf, dul.Event))
g.add((smartManufacturing.Idle, RDFS.subClassOf, dul.Event))

# Read the data file
# index_col=False, 
data = pd.read_excel("./Cycle_Data_with_Substates_Complete.xlsx", sheet_name='Data', dtype='unicode') 

# tmp=data
tmp = data[data['CycleState']=='8']

# Mapping cycleState to their description
mapping_cycleState = {
"1":"R01 Picks Tray from MHS",
"2":"R01 Places Tray on Conveyor",
"3":"R01 Back to Home Position and Conveyors On",
"4":"R02 Pick Body 1 from Conveyor",
"5":"R02 Place Body 1 on local station",
"6":"R02 Pick Body 2 from Conveyor",
"7":"R02 Place Body 2 on local station",
"8":"R02 and R03 Assemble Rocket Together",
"9":"Conveyors move assembled rocket to R04 and R04 picks up tray",
"10":"R04 place tray on fixture",
"11":"R04 Disassemble Nose",
"12":"R04 Disassemble Body 2",
"13":"R04 Disassemble Body 1",
"14":"R04 Disassemble Tail",
"15":"R04 Place Tail Back on Tray",
"16":"R04 Place Nose Back on Tray",
"17":"R04 Place Body 1 Back on Tray",
"18":"R04 Place Body 2 Back on Tray",
"19":"R04 Pick Disassembled Tray",
"20":"R04 Place Tray on MHS",
"21":"R04 Back to Home Position"
}

tmp["cycleState_Mapping"] = tmp["CycleState"].replace(mapping_cycleState)

# Mapping R02 Substate function
mapping_R02SubState = {
"0":"R02 Pick Body 1 From Fixture",
"1":"R02 Offers Body 1 To R03",
"2":"R02 Pick Body 2 From Fixture",
"3":"R02 Offers Body 2 To R03",
"4":"R02 Return To Home Position"
}
tmp["R02_Substate_Mapping"] = tmp["R02_Substate"].replace(mapping_R02SubState)

# Mapping R02 Substate to their class URI
mapping_R02SubState_URI = {
"0":rdflib.term.URIRef("http://purl.org/net/SmartManufacturing/v00/R02_Pick_Body1_From_Fixture"),
"1":rdflib.term.URIRef("http://purl.org/net/SmartManufacturing/v00/R02_Offers_Body1_To_R03"),
"2":rdflib.term.URIRef("http://purl.org/net/SmartManufacturing/v00/R02_Pick_Body2_From_Fixture"),
"3":rdflib.term.URIRef("http://purl.org/net/SmartManufacturing/v00/R02_Offers_Body2_To_R03"),
"4":rdflib.term.URIRef("http://purl.org/net/SmartManufacturing/v00/R02_Return_To_Home_Position")
}

mapping_R02SubState_NoURI = {
"0":("http://purl.org/net/SmartManufacturing/v00/R02_Pick_Body1_From_Fixture"),
"1":("http://purl.org/net/SmartManufacturing/v00/R02_Offers_Body1_To_R03"),
"2":("http://purl.org/net/SmartManufacturing/v00/R02_Pick_Body2_From_Fixture"),
"3":("http://purl.org/net/SmartManufacturing/v00/R02_Offers_Body2_To_R03"),
"4":("http://purl.org/net/SmartManufacturing/v00/R02_Return_To_Home_Position")
}

# R02 and R03 substates
g.add((smartManufacturing.R02SubState, RDFS.subClassOf, dul.Event))
g.add((smartManufacturing.R03SubState, RDFS.subClassOf, dul.Event))

# R02 substates defined as class
g.add((smartManufacturing.R02_Pick_Body1_From_Fixture, RDFS.subClassOf, smartManufacturing.R02SubState))
g.add((smartManufacturing.R02_Pick_Body1_From_Fixture, rdflib.term.URIRef('http://www.w3.org/2000/01/rdf-schema#label'), rdflib.term.Literal(str("R02 Pick Body 1 From Fixture"))))

g.add((smartManufacturing.R02_Offers_Body1_To_R03, RDFS.subClassOf, smartManufacturing.R02SubState))
g.add((smartManufacturing.R02_Offers_Body1_To_R03, rdflib.term.URIRef('http://www.w3.org/2000/01/rdf-schema#label'), rdflib.term.Literal(str("R02 Offers Body 1 To R03"))))

g.add((smartManufacturing.R02_Pick_Body2_From_Fixture, RDFS.subClassOf, smartManufacturing.R02SubState))
g.add((smartManufacturing.R02_Pick_Body2_From_Fixture, rdflib.term.URIRef('http://www.w3.org/2000/01/rdf-schema#label'), rdflib.term.Literal(str("R02 Pick Body 2 From Fixture"))))

g.add((smartManufacturing.R02_Offers_Body2_To_R03, RDFS.subClassOf, smartManufacturing.R02SubState))
g.add((smartManufacturing.R02_Offers_Body2_To_R03, rdflib.term.URIRef('http://www.w3.org/2000/01/rdf-schema#label'), rdflib.term.Literal(str("R02 Offers Body 2 To R03"))))

g.add((smartManufacturing.R02_Return_To_Home_Position, RDFS.subClassOf, smartManufacturing.R02SubState))
g.add((smartManufacturing.R02_Return_To_Home_Position, rdflib.term.URIRef('http://www.w3.org/2000/01/rdf-schema#label'), rdflib.term.Literal(str("R02 Return To Home Position"))))

# R03 substates defined as class
g.add((smartManufacturing.R03_Pick_Tail_From_Tray, RDFS.subClassOf, smartManufacturing.R03SubState))
g.add((smartManufacturing.R03_Pick_Tail_From_Tray, rdflib.term.URIRef('http://www.w3.org/2000/01/rdf-schema#label'), rdflib.term.Literal(str("R03 Pick Tail From Tray"))))

g.add((smartManufacturing.R03_Place_Tail_On_Fixture, RDFS.subClassOf, smartManufacturing.R03SubState))
g.add((smartManufacturing.R03_Place_Tail_On_Fixture, rdflib.term.URIRef('http://www.w3.org/2000/01/rdf-schema#label'), rdflib.term.Literal(str("R03 Place Tail On Fixture"))))

g.add((smartManufacturing.R03_Receive_Body1_From_R02, RDFS.subClassOf, smartManufacturing.R03SubState))
g.add((smartManufacturing.R03_Receive_Body1_From_R02, rdflib.term.URIRef('http://www.w3.org/2000/01/rdf-schema#label'), rdflib.term.Literal(str("R03 Receive Body 1 From R02"))))

g.add((smartManufacturing.R03_Assemble_Body1, RDFS.subClassOf, smartManufacturing.R03SubState))
g.add((smartManufacturing.R03_Assemble_Body1, rdflib.term.URIRef('http://www.w3.org/2000/01/rdf-schema#label'), rdflib.term.Literal(str("R03 Assemble Body 1"))))

g.add((smartManufacturing.R03_Receive_Body2_From_R02, RDFS.subClassOf, smartManufacturing.R03SubState))
g.add((smartManufacturing.R03_Receive_Body2_From_R02, rdflib.term.URIRef('http://www.w3.org/2000/01/rdf-schema#label'), rdflib.term.Literal(str("R03 Receive Body 2 From R02"))))

g.add((smartManufacturing.R03_Assemble_Body2, RDFS.subClassOf, smartManufacturing.R03SubState))
g.add((smartManufacturing.R03_Assemble_Body2, rdflib.term.URIRef('http://www.w3.org/2000/01/rdf-schema#label'), rdflib.term.Literal(str("R03 Assemble Body 2"))))

g.add((smartManufacturing.R03_Pick_Nose_From_Tray, RDFS.subClassOf, smartManufacturing.R03SubState))
g.add((smartManufacturing.R03_Pick_Nose_From_Tray, rdflib.term.URIRef('http://www.w3.org/2000/01/rdf-schema#label'), rdflib.term.Literal(str("R03 Pick Nose From Tray"))))

g.add((smartManufacturing.R03_Assemble_Nose, RDFS.subClassOf, smartManufacturing.R03SubState))
g.add((smartManufacturing.R03_Assemble_Nose, rdflib.term.URIRef('http://www.w3.org/2000/01/rdf-schema#label'), rdflib.term.Literal(str("R03 Assemble Nose"))))

g.add((smartManufacturing.R03_Pick_And_Place_Assembled_Rocket_On_Tray, RDFS.subClassOf, smartManufacturing.R03SubState))
g.add((smartManufacturing.R03_Pick_And_Place_Assembled_Rocket_On_Tray, rdflib.term.URIRef('http://www.w3.org/2000/01/rdf-schema#label'), rdflib.term.Literal(str("R03 Pick And Place Assembled Rocket On Tray"))))

g.add((smartManufacturing.R03_Return_To_Home_Position, RDFS.subClassOf, smartManufacturing.R03SubState))
g.add((smartManufacturing.R03_Return_To_Home_Position, rdflib.term.URIRef('http://www.w3.org/2000/01/rdf-schema#label'), rdflib.term.Literal(str("R03 Return To Home Position"))))

# Mapping R03 Substate function
mapping_R03SubState = {
"0":"R03 Pick Tail From Tray",
"1":"R03 Place Tail On Fixture",
"2":"R03 Receive Body 1 From R02",
"3":"R03 Assemble Body 1",
"4":"R03 Receive Body 2 From R02",
"5":"R03 Assemble Body 2",
"6":"R03 Pick Nose From Tray",
"7":"R03 Assemble Nose",
"8":"R03 Pick And Place Assembled Rocket On Tray",
"9":"R03 Return To Home Position"
}
tmp["R03_Substate_Mapping"] = tmp["R03_Substate"].replace(mapping_R03SubState)

# Mapping R03 Substate to their class URI
mapping_R03SubState_URI = {
"0":rdflib.term.URIRef("http://purl.org/net/SmartManufacturing/v00/R03_Pick_Tail_From_Tray"),
"1":rdflib.term.URIRef("http://purl.org/net/SmartManufacturing/v00/R03_Place_Tail_On_Fixture"),
"2":rdflib.term.URIRef("http://purl.org/net/SmartManufacturing/v00/R03_Receive_Body1_From_R02"),
"3":rdflib.term.URIRef("http://purl.org/net/SmartManufacturing/v00/R03_Assemble_Body1"),
"4":rdflib.term.URIRef("http://purl.org/net/SmartManufacturing/v00/R03_Receive_Body2_From_R02"),
"5":rdflib.term.URIRef("http://purl.org/net/SmartManufacturing/v00/R03_Assemble_Body2"),
"6":rdflib.term.URIRef("http://purl.org/net/SmartManufacturing/v00/R03_Pick_Nose_From_Tray"),
"7":rdflib.term.URIRef("http://purl.org/net/SmartManufacturing/v00/R03_Assemble_Nose"),
"8":rdflib.term.URIRef("http://purl.org/net/SmartManufacturing/v00/R03_Pick_And_Place_Assembled_Rocket_On_Tray"),
"9":rdflib.term.URIRef("http://purl.org/net/SmartManufacturing/v00/R03_Return_To_Home_Position")
}

mapping_R03SubState_NoURI = {
"0":("http://purl.org/net/SmartManufacturing/v00/R03_Pick_Tail_From_Tray"),
"1":("http://purl.org/net/SmartManufacturing/v00/R03_Place_Tail_On_Fixture"),
"2":("http://purl.org/net/SmartManufacturing/v00/R03_Receive_Body1_From_R02"),
"3":("http://purl.org/net/SmartManufacturing/v00/R03_Assemble_Body1"),
"4":("http://purl.org/net/SmartManufacturing/v00/R03_Receive_Body2_From_R02"),
"5":("http://purl.org/net/SmartManufacturing/v00/R03_Assemble_Body2"),
"6":("http://purl.org/net/SmartManufacturing/v00/R03_Pick_Nose_From_Tray"),
"7":("http://purl.org/net/SmartManufacturing/v00/R03_Assemble_Nose"),
"8":("http://purl.org/net/SmartManufacturing/v00/R03_Pick_And_Place_Assembled_Rocket_On_Tray"),
"9":("http://purl.org/net/SmartManufacturing/v00/R03_Return_To_Home_Position")
}

# A cycle state is a sequence
# Look into cycle state 8
for cycleCount in tmp.CycleCount.unique():
    for cycle in cycleCount:
        tmp_cycle=tmp[tmp.CycleCount==cycle]
#         print(cycle, tmp_cycle[1:]._time.iloc[0], tmp_cycle[-1:]._time.iloc[0])
        # cycle count sequence has start time, end time
#         cycleStartTime = tmp_cycle.iloc[0]._time #tmp_cycle.iloc[tmp_cycle.head(1).index[0]]._time
#         cycleEndTime = tmp_cycle.iloc[-1]._time #tmp_cycle.iloc[tmp_cycle.tail(1).index[0]]._time
        
#         cycleStartTime = tmp_cycle.iloc[tmp_cycle.head(1).index[0]]._time
#         cycleEndTime = tmp_cycle.iloc[tmp_cycle.tail(1).index[0]]._time
        
#         cycleStartTime = tmp_cycle[1:]._time.iloc[0]
#         cycleEndTime = tmp_cycle[-1:]._time.iloc[0]
        
        cycleCount = URIRef(smartManufacturingData+str(uuid.uuid4()))   
        g.add((cycleCount, RDF.type, scene.Scene))
#         g.add((cycleCount, scene.startTime, rdflib.term.Literal(cycleStartTime)))
#         g.add((cycleCount, scene.endTime, rdflib.term.Literal(cycleEndTime)))
        g.add((cycleCount, rdflib.term.URIRef('http://www.w3.org/2000/01/rdf-schema#label'), rdflib.term.Literal(str(cycle))))

        for state in tmp_cycle.CycleState.unique():
#             if state=="8":
                tmp_cycleState=tmp[tmp.CycleState==state]
    
                # cycle state sequence has start time, end time
#                 cycleStateStartTime = tmp_cycleState.iloc[0]._time #tmp_cycle.iloc[tmp_cycle.head(1).index[0]]._time
#                 cycleStateEndTime = tmp_cycleState.iloc[-1]._time #tmp_cycle.iloc[tmp_cycle.tail(1).index[0]]._time
#                 cycleStartTime = tmp_cycle.iloc[tmp_cycle.head(1).index[0]]._time
#                 cycleEndTime = tmp_cycle.iloc[tmp_cycle.tail(1).index[0]]._time
                
#                 cycleStateStartTime = tmp_cycle[1:]._time.iloc[0]
#                 cycleStateEndTime = tmp_cycle[-1:]._time.iloc[0]
            
                cycleState = URIRef(smartManufacturingData+str(uuid.uuid4()))  
                g.add((cycleState, RDF.type, scene.Frame))
                g.add((cycleState, scene.isPartOf, cycleCount))
#                 g.add((cycleState, scene.startTime, rdflib.term.Literal(cycleStateStartTime)))
#                 g.add((cycleState, scene.endTime, rdflib.term.Literal(cycleStateEndTime)))
                g.add((cycleState, rdflib.term.URIRef('http://www.w3.org/2000/01/rdf-schema#label'), rdflib.term.Literal(str(state))))
    
                if str(tmp_cycleState.Description) == "NoNose":
                    descript = URIRef(smartManufacturingData+str(uuid.uuid4()))
                    g.add((descript, RDF.type, smartManufacturingData.NoNose))
                    g.add((cycleState, smartManufacturingData.hasAnomaly, descript))
                if str(tmp_cycleState.Description) == "NoNose,NoBody2":
                    descript = URIRef(smartManufacturingData+str(uuid.uuid4()))
                    g.add((descript, RDF.type, smartManufacturingData.NoNoseNoBody2))
                    g.add((cycleState, smartManufacturingData.hasAnomaly, descript))
                if str(tmp_cycleState.Description) == "NoNose,NoBody2,NoBody1":
                    descript = URIRef(smartManufacturingData+str(uuid.uuid4()))
                    g.add((descript, RDF.type, smartManufacturingData.NoNoseNoBody2NoBody1))
                    g.add((cycleState, smartManufacturingData.hasAnomaly, descript))
    
                for i in tmp_cycleState.itertuples():
                    gripperLoad2 = URIRef(smartManufacturingData+str(uuid.uuid4()))
                    g.add((gripperLoad2, RDF.type, sosa.Observation))
                    g.add((gripperLoad2, sosa.hasSimpleResult,rdflib.term.Literal(i.R02_LoadCell)))
                    g.add((gripperLoad2, sosa.madeBySensor,load2))
                    
                    gripperLoad3 = URIRef(smartManufacturingData+str(uuid.uuid4()))
                    g.add((gripperLoad3, RDF.type, sosa.Observation))
                    g.add((gripperLoad3, sosa.hasSimpleResult,rdflib.term.Literal(i.R03_LoadCell)))
                    g.add((gripperLoad3, sosa.madeBySensor,load3))
                                 
                    gripperPot1 = URIRef(smartManufacturingData+str(uuid.uuid4()))
                    g.add((gripperPot1, RDF.type,  sosa.Observation))
                    g.add((gripperPot1, sosa.hasSimpleResult,rdflib.term.Literal(i.R01_Potentiometer)))
                    g.add((gripperPot1, sosa.madeBySensor,potentiometer1))
                    
                    gripperPot2 = URIRef(smartManufacturingData+str(uuid.uuid4()))
                    g.add((gripperPot2, RDF.type,  sosa.Observation))
                    g.add((gripperPot2, sosa.hasSimpleResult,rdflib.term.Literal(i.R02_Potentiometer)))
                    g.add((gripperPot2, sosa.madeBySensor,potentiometer2))
                    
                    gripperPot3 = URIRef(smartManufacturingData+str(uuid.uuid4()))
                    g.add((gripperPot3, RDF.type,  sosa.Observation))
                    g.add((gripperPot3, sosa.hasSimpleResult,rdflib.term.Literal(i.R03_Potentiometer)))
                    g.add((gripperPot3, sosa.madeBySensor,potentiometer3))
                    
                    gripperPot4 = URIRef(smartManufacturingData+str(uuid.uuid4()))
                    g.add((gripperPot4, RDF.type,  sosa.Observation))
                    g.add((gripperPot4, sosa.hasSimpleResult,rdflib.term.Literal(i.R04_Potentiometer)))
                    g.add((gripperPot4, sosa.madeBySensor,potentiometer4))
                        
                    if int(i.R02_LoadCell)>=1700  and int(i.R02_LoadCell) <=1750 :
                        g.add((gripperLoad2, RDF.type, smartManufacturing.Idle))
                    if int(i.R03_LoadCell)>=1700  and int(i.R03_LoadCell) <=1750 :
                        g.add((gripperLoad3, RDF.type, smartManufacturing.Idle))
                    
                    if int(i.R02_LoadCell)>=10200  and int(i.R02_LoadCell) <=10300 :
                        g.add((gripperLoad2, RDF.type, smartManufacturing.ClosedWithPart))
                    if int(i.R03_LoadCell)>=10200  and int(i.R03_LoadCell) <=10300 :
                        g.add((gripperLoad3, RDF.type, smartManufacturing.ClosedWithPart))
    
                    if int(i.R01_Potentiometer)==1900:
                        g.add((gripperPot1, RDF.type, smartManufacturing.Open))
                    if int(i.R01_Potentiometer)>=11500 and int(i.R01_Potentiometer)<=11600:
                        g.add((gripperPot1, RDF.type, smartManufacturing.ClosedWithPart))
                    if int(i.R02_Potentiometer)==1900:
                        g.add((gripperPot2, RDF.type, smartManufacturing.Open))
                    if int(i.R02_Potentiometer)>=11500 and int(i.R02_Potentiometer)<=11600:
                        g.add((gripperPot2, RDF.type, smartManufacturing.ClosedWithPart))
                    if int(i.R03_Potentiometer)==1900:
                        g.add((gripperPot3, RDF.type, smartManufacturing.Open))
                    if int(i.R03_Potentiometer)>=11500 and int(i.R03_Potentiometer)<=11600:
                        g.add((gripperPot3, RDF.type, smartManufacturing.ClosedWithPart))
                    if int(i.R04_Potentiometer)==1900:
                        g.add((gripperPot4, RDF.type, smartManufacturing.Open))
                    if int(i.R04_Potentiometer)>=11500 and int(i.R04_Potentiometer)<=11600:
                        g.add((gripperPot4, RDF.type, smartManufacturing.ClosedWithPart))
                    
                    angleSJoint2 = URIRef(smartManufacturingData+str(uuid.uuid4()))
                    g.add((angleSJoint2, RDF.type, sosa.Observation))
                    g.add((angleSJoint2, sosa.hasSimpleResult,rdflib.term.Literal(i.M_R02_SJointAngle_Degree)))
                    g.add((angleSJoint2,sosa.observedProperty, angle))
                    g.add((angleSJoint2, sosa.hasFeatureOfInterestOf,robotSJoint2))
                    
                    angleSJoint3 = URIRef(smartManufacturingData+str(uuid.uuid4()))
                    g.add((angleSJoint3, RDF.type, sosa.Observation))
                    g.add((angleSJoint3, sosa.hasSimpleResult,rdflib.term.Literal(i.M_R03_SJointAngle_Degree)))
                    g.add((angleSJoint3,sosa.observedProperty, angle))
                    g.add((angleSJoint3, sosa.hasFeatureOfInterestOf,robotSJoint3))
                    
                    safety1 = URIRef(smartManufacturingData+str(uuid.uuid4()))
                    g.add((safety1, RDF.type, sosa.Observation))
                    g.add((safety1, sosa.hasSimpleResult,rdflib.term.Literal(i.Door1_Safety)))
                    g.add((safety1, sosa.madeBySensor,safetyDoor1))
                    
                    safety2 = URIRef(smartManufacturingData+str(uuid.uuid4()))
                    g.add((safety2, sosa.hasSimpleResult,rdflib.term.Literal(i.Door2_Safety)))
                    g.add((safety2, sosa.madeBySensor,safetyDoor2))
                    
                    hmi = URIRef(smartManufacturingData+str(uuid.uuid4()))
                    g.add((hmi, RDF.type, sosa.Observation))
                    g.add((hmi, sosa.hasSimpleResult,rdflib.term.Literal(i.HMIESTOP)))
                    g.add((hmi, sosa.madeBySensor,HMIEStopButton))
                    
                    g.add((cycleState, scene.includes,gripperLoad2))
                    g.add((cycleState, scene.includes,gripperLoad3))
                    
                    g.add((cycleState, scene.includes,gripperPot1))
                    g.add((cycleState, scene.includes,gripperPot2))
                    g.add((cycleState, scene.includes,gripperPot3))
                    g.add((cycleState, scene.includes,gripperPot4))
                    
                    g.add((cycleState, scene.includes,angleSJoint2))
                    g.add((cycleState, scene.includes,angleSJoint3))
                    
                    g.add((cycleState, scene.includes,safety1))
                    g.add((cycleState, scene.includes,safety2))
                    g.add((cycleState, scene.includes,hmi))
                    
                    # Create an UUID for the R02 and R03 Substates
                    if (i.R02_Substate) in list(mapping_R02SubState.keys()):
                        r02 = URIRef(smartManufacturingData+str(uuid.uuid4()))
                        r02_label = rdflib.term.URIRef('http://purl.org/net/SmartManufacturing/v00/'+mapping_R02SubState.get(i.R02_Substate).replace(" ","_"))
                        g.add((r02, RDF.type, r02_label))
                        
                    if (i.R03_Substate) in list(mapping_R03SubState.keys()):
                        r03 = URIRef(smartManufacturingData+str(uuid.uuid4()))
                        r03_label = rdflib.term.URIRef('http://purl.org/net/SmartManufacturing/v00/'+mapping_R03SubState.get(i.R03_Substate).replace(" ","_"))
                        g.add((r03, RDF.type, r03_label))
                       
                    # Substate	causes 	Substate
                    # R02_0		        R03_0
                    # from math import nan
                    # if (i.R02_Substate_Mapping is not nan) or (i.R03_Substate_Mapping is not nan) or (mapping_R02SubState.keys() is not nan) or (mapping_R02SubState.values() is not nan) or (mapping_R03SubState.keys() is not nan) or (mapping_R03SubState.values() is not nan): 
                    if (i.R02_Substate is not np.nan) and (i.R03_Substate is not np.nan): 
                        # print(i.R02_Substate, i.R03_Substate)
                        # print(type(i.R02_Substate), type(i.R03_Substate))
                        # break 
                        
                        if str(list(mapping_R02SubState.keys())[list(mapping_R02SubState.values()).index(i.R02_Substate_Mapping)]) == "0" and str(list(mapping_R03SubState.keys())[list(mapping_R03SubState.values()).index(i.R03_Substate_Mapping)]) == "0":
                            g.add((r02, causal.causes, r03))
                            causesTypeLabel = rdflib.term.URIRef('http://purl.org/net/SmartManufacturing/v00/'+(mapping_R03SubState.get("0").replace(" ","_")))
                            causedByTypeLabel = rdflib.term.URIRef('http://purl.org/net/SmartManufacturing/v00/'+(mapping_R02SubState.get("0").replace(" ","_")))
                            g.add((r02, causal.causesType, causesTypeLabel))
                            g.add((r03, causal.causedByType, causedByTypeLabel))
    
                        # Substate	causes 	Substate
                        # R03_1		        R02_1
                        if str(list(mapping_R02SubState.keys())[list(mapping_R02SubState.values()).index(i.R02_Substate_Mapping)]) == "1" and str(list(mapping_R03SubState.keys())[list(mapping_R03SubState.values()).index(i.R03_Substate_Mapping)]) == "1":
                            g.add((r03, causal.causes, r02))
                            causesTypeLabel = rdflib.term.URIRef('http://purl.org/net/SmartManufacturing/v00/'+(mapping_R02SubState.get("1").replace(" ","_")))
                            causedByTypeLabel = rdflib.term.URIRef('http://purl.org/net/SmartManufacturing/v00/'+(mapping_R03SubState.get("1").replace(" ","_")))
                            g.add((r03, causal.causesType, causesTypeLabel))
                            g.add((r02, causal.causedByType, causedByTypeLabel))
    
                        # Substate	causes 	Substate
                        # R03_2		        R02_2
                        if str(list(mapping_R02SubState.keys())[list(mapping_R02SubState.values()).index(i.R02_Substate_Mapping)]) == "2" and str(list(mapping_R03SubState.keys())[list(mapping_R03SubState.values()).index(i.R03_Substate_Mapping)]) == "2":
                            g.add((r03, causal.causes, r02))
                            causesTypeLabel = rdflib.term.URIRef('http://purl.org/net/SmartManufacturing/v00/'+(mapping_R02SubState.get("2").replace(" ","_")))
                            causedByTypeLabel = rdflib.term.URIRef('http://purl.org/net/SmartManufacturing/v00/'+(mapping_R03SubState.get("2").replace(" ","_")))
                            g.add((r03, causal.causesType, causesTypeLabel))
                            g.add((r02, causal.causedByType, causedByTypeLabel))
    
                        # Substate	causes 	Substate
                        # R03_4		        R02_4
                        if str(list(mapping_R02SubState.keys())[list(mapping_R02SubState.values()).index(i.R02_Substate_Mapping)]) == "4" and str(list(mapping_R03SubState.keys())[list(mapping_R03SubState.values()).index(i.R03_Substate_Mapping)]) == "4":
                            g.add((r03, causal.causes, r02))
                            causesTypeLabel = rdflib.term.URIRef('http://purl.org/net/SmartManufacturing/v00/'+(mapping_R02SubState.get("4").replace(" ","_")))
                            causedByTypeLabel = rdflib.term.URIRef('http://purl.org/net/SmartManufacturing/v00/'+(mapping_R03SubState.get("4").replace(" ","_")))
                            g.add((r03, causal.causesType, causesTypeLabel))
                            g.add((r02, causal.causedByType, causedByTypeLabel))


                        g.add((cycleState, scene.includes,r02))
                        g.add((cycleState, scene.includes,r03))
                    
                            
for frames in g.subjects(RDF.type, scene.Frame):
    event2 = dict()
    event3 = dict()
    event2List = list()
    event3List = list()
        
    for events in g.objects(frames, scene.includes):
        # Get the Substates 
        for eventType in g.objects(events, RDF.type):
            if str(eventType) in list(mapping_R02SubState_NoURI.values()):
                event2[events] = eventType
            if str(eventType) in list(mapping_R03SubState_NoURI.values()):
                event3[events]= eventType
                
    event2_0, event2_1, event2_2, event2_3, event2_4 = list(),list(),list(),list(),list()           
    event3_0, event3_1, event3_2, event3_3, event3_4, event3_5, event3_6, event3_7, event3_8, event3_9 = list(),list(),list(),list(),list(),list(),list(),list(),list(),list()            
    
    for k2,v2 in event3.items():
        for k1,v1 in list(mapping_R03SubState_URI.items()):
            if v1 in v2:
                # print("eventUUID:",str(k2)," EventName:",str(mapping_R03SubState_NoURI[str(k1)])," Event# in Dict:",k1)
                if k1 == "0":
                    event3_0.append(k2)
                if k1 == "1":
                    event3_1.append(k2)
                if k1 == "2":
                    event3_2.append(k2)
                if k1 == "3":
                    event3_3.append(k2)
                if k1 == "4":
                    event3_4.append(k2)
                if k1 == "5":
                    event3_5.append(k2)
                if k1 == "6":
                    event3_6.append(k2)
                if k1 == "7":
                    event3_7.append(k2)
                if k1 == "8":
                    event3_8.append(k2)
                if k1 == "9":
                    event3_9.append(k2)
    
    for k2,v2 in event2.items():
        for k1,v1 in list(mapping_R02SubState_URI.items()):
            if v1 in v2:
                # print("eventUUID:",str(k2)," EventName:",str(mapping_R03SubState_NoURI[str(k1)])," Event# in Dict:",k1)
                if k1 == "0":
                    event2_0.append(k2)
                if k1 == "1":
                    event2_1.append(k2)
                if k1 == "2":
                    event2_2.append(k2)
                if k1 == "3":
                    event2_3.append(k2)
                if k1 == "4":
                    event2_4.append(k2)
                    
    # Substate	causes 	Substate
    # R02_0		        R02_1
    for a in event2_0:
        for b in event2_1:
            g.add((a, causal.causes, b))
            causesTypeLabel = rdflib.term.URIRef('http://purl.org/net/SmartManufacturing/v00/'+(mapping_R02SubState.get("1").replace(" ","_")))
            causedByTypeLabel = rdflib.term.URIRef('http://purl.org/net/SmartManufacturing/v00/'+(mapping_R02SubState.get("0").replace(" ","_")))
            g.add((a, causal.causesType, causesTypeLabel))
            g.add((b, causal.causedByType, causedByTypeLabel))
    
    # Substate	causes 	Substate
    # R02_1		        R02_2
    for a in event2_1:
        for b in event2_2:
            g.add((a, causal.causes, b))
            causesTypeLabel = rdflib.term.URIRef('http://purl.org/net/SmartManufacturing/v00/'+(mapping_R02SubState.get("2").replace(" ","_")))
            causedByTypeLabel = rdflib.term.URIRef('http://purl.org/net/SmartManufacturing/v00/'+(mapping_R02SubState.get("1").replace(" ","_")))
            g.add((a, causal.causesType, causesTypeLabel))
            g.add((b, causal.causedByType, causedByTypeLabel))
    
    # Substate	causes 	Substate
    # R02_2		        R02_3
    for a in event2_2:
        for b in event2_3:
            g.add((a, causal.causes, b))
            causesTypeLabel = rdflib.term.URIRef('http://purl.org/net/SmartManufacturing/v00/'+(mapping_R02SubState.get("3").replace(" ","_")))
            causedByTypeLabel = rdflib.term.URIRef('http://purl.org/net/SmartManufacturing/v00/'+(mapping_R02SubState.get("2").replace(" ","_")))
            g.add((a, causal.causesType, causesTypeLabel))
            g.add((b, causal.causedByType, causedByTypeLabel))
    
    # Substate	causes 	Substate
    # R02_3	        R02_4
    for a in event2_3:
        for b in event2_4:
            g.add((a, causal.causes, b))
            causesTypeLabel = rdflib.term.URIRef('http://purl.org/net/SmartManufacturing/v00/'+(mapping_R02SubState.get("4").replace(" ","_")))
            causedByTypeLabel = rdflib.term.URIRef('http://purl.org/net/SmartManufacturing/v00/'+(mapping_R02SubState.get("5").replace(" ","_")))
            g.add((a, causal.causesType, causesTypeLabel))
            g.add((b, causal.causedByType, causedByTypeLabel))

    # Substate	causes 	Substate
    # R03_0		        R03_1
    for a in event3_0:
        for b in event3_1:
            g.add((a, causal.causes, b))
            causesTypeLabel = rdflib.term.URIRef('http://purl.org/net/SmartManufacturing/v00/'+(mapping_R03SubState.get("1").replace(" ","_")))
            causedByTypeLabel = rdflib.term.URIRef('http://purl.org/net/SmartManufacturing/v00/'+(mapping_R03SubState.get("0").replace(" ","_")))
            g.add((a, causal.causesType, causesTypeLabel))
            g.add((b, causal.causedByType, causedByTypeLabel))
    
    # Substate	causes 	Substate
    # R03_1		        R03_2
    for a in event3_1:
        for b in event3_2:
            g.add((a, causal.causes, b))
            causesTypeLabel = rdflib.term.URIRef('http://purl.org/net/SmartManufacturing/v00/'+(mapping_R03SubState.get("2").replace(" ","_")))
            causedByTypeLabel = rdflib.term.URIRef('http://purl.org/net/SmartManufacturing/v00/'+(mapping_R03SubState.get("1").replace(" ","_")))
            g.add((a, causal.causesType, causesTypeLabel))
            g.add((b, causal.causedByType, causedByTypeLabel))
    
    # Substate	causes 	Substate
    # R03_2		        R03_3
    for a in event3_2:
        for b in event3_3:
            g.add((a, causal.causes, b))
            causesTypeLabel = rdflib.term.URIRef('http://purl.org/net/SmartManufacturing/v00/'+(mapping_R03SubState.get("3").replace(" ","_")))
            causedByTypeLabel = rdflib.term.URIRef('http://purl.org/net/SmartManufacturing/v00/'+(mapping_R03SubState.get("2").replace(" ","_")))
            g.add((a, causal.causesType, causesTypeLabel))
            g.add((b, causal.causedByType, causedByTypeLabel))
    
    # Substate	causes 	Substate
    # R03_3	        R03_4
    for a in event3_3:
        for b in event3_4:
            g.add((a, causal.causes, b))
            causesTypeLabel = rdflib.term.URIRef('http://purl.org/net/SmartManufacturing/v00/'+(mapping_R03SubState.get("4").replace(" ","_")))
            causedByTypeLabel = rdflib.term.URIRef('http://purl.org/net/SmartManufacturing/v00/'+(mapping_R03SubState.get("3").replace(" ","_")))
            g.add((a, causal.causesType, causesTypeLabel))
            g.add((b, causal.causedByType, causedByTypeLabel))
    
    # Substate	causes 	Substate
    # R03_4		        R03_5
    for a in event3_4:
        for b in event3_5:
            g.add((a, causal.causes, b))
            causesTypeLabel = rdflib.term.URIRef('http://purl.org/net/SmartManufacturing/v00/'+(mapping_R03SubState.get("5").replace(" ","_")))
            causedByTypeLabel = rdflib.term.URIRef('http://purl.org/net/SmartManufacturing/v00/'+(mapping_R03SubState.get("4").replace(" ","_")))
            g.add((a, causal.causesType, causesTypeLabel))
            g.add((b, causal.causedByType, causedByTypeLabel))
    
    # Substate	causes 	Substate
    # R03_5		        R03_6
    for a in event3_5:
        for b in event3_6:
            g.add((a, causal.causes, b))
            causesTypeLabel = rdflib.term.URIRef('http://purl.org/net/SmartManufacturing/v00/'+(mapping_R03SubState.get("6").replace(" ","_")))
            causedByTypeLabel = rdflib.term.URIRef('http://purl.org/net/SmartManufacturing/v00/'+(mapping_R03SubState.get("5").replace(" ","_")))
            g.add((a, causal.causesType, causesTypeLabel))
            g.add((b, causal.causedByType, causedByTypeLabel))
    
    # Substate	causes 	Substate
    # R03_6		        R03_7
    for a in event3_6:
        for b in event3_7:
            g.add((a, causal.causes, b))
            causesTypeLabel = rdflib.term.URIRef('http://purl.org/net/SmartManufacturing/v00/'+(mapping_R03SubState.get("7").replace(" ","_")))
            causedByTypeLabel = rdflib.term.URIRef('http://purl.org/net/SmartManufacturing/v00/'+(mapping_R03SubState.get("6").replace(" ","_")))
            g.add((a, causal.causesType, causesTypeLabel))
            g.add((b, causal.causedByType, causedByTypeLabel))
            
    # Substate	causes 	Substate
    # R03_7		        R03_8
    for a in event3_5:
        for b in event3_6:
            g.add((a, causal.causes, b))
            causesTypeLabel = rdflib.term.URIRef('http://purl.org/net/SmartManufacturing/v00/'+(mapping_R03SubState.get("8").replace(" ","_")))
            causedByTypeLabel = rdflib.term.URIRef('http://purl.org/net/SmartManufacturing/v00/'+(mapping_R03SubState.get("7").replace(" ","_")))
            g.add((a, causal.causesType, causesTypeLabel))
            g.add((b, causal.causedByType, causedByTypeLabel))
    
    # Substate	causes 	Substate
    # R03_8		        R03_9
    for a in event3_8:
        for b in event3_9:
            g.add((a, causal.causes, b))
            causesTypeLabel = rdflib.term.URIRef('http://purl.org/net/SmartManufacturing/v00/'+(mapping_R03SubState.get("9").replace(" ","_")))
            causedByTypeLabel = rdflib.term.URIRef('http://purl.org/net/SmartManufacturing/v00/'+(mapping_R03SubState.get("8").replace(" ","_")))
            g.add((a, causal.causesType, causesTypeLabel))
            g.add((b, causal.causedByType, causedByTypeLabel))


# g.serialize("CausalKGSmartManufacturing_CycleState8.ttl", format="n3")
g.serialize("CausalKGSmartManufacturing_CompleteData_CycleState8_NoTime.ttl", format="n3")
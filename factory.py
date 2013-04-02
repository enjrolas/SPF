class Point:
    """points of interest on a solar panel"""
    panelId=0
    pointType=""
    position=0
    remainingDistance=0

class Panel:
    """Panel data structure"""
    panelId=0
    targetCurrent=0
    targetVoltage=0
    testCurrent=0
    testVoltage=0
    status="queued"

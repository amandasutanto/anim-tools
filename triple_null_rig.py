import maya.cmds as cmds

def triple_null_rig():
    """A function to create 3 stacks of NURBS circles in different sizes to aid in animating props.

    Returns:
        str: Last user selection
    """

    user_clicks = cmds.ls(selection=True)

    if len(user_clicks) == 1:
        #Creating the 3 circles
        cmds.circle(nr=(0, 1, 0), c=(0, 0, 0), r=7, n=user_clicks[0] + "_parentConstraint") #outer circle
        cmds.circle(nr=(0, 1, 0), c=(0, 0, 0), r=5, n=user_clicks[0] + "_animate") #middle circle
        cmds.circle(nr=(0, 1, 0), c=(0, 0, 0), r=3, n=user_clicks[0] + "_childConstraint") #inner circle

        #Creating an empty group to house the 3 circle rig and a temporary locator to help with parent constraint
        cmds.group(em=True, n=user_clicks[0] + "_tripleNullRigGrp")
        cmds.spaceLocator(n="tempLocator")

        #Snapping each items to user selected position with parent constraint.
        #It inherits the position and parent constraint connection.
        cmds.parentConstraint(user_clicks[0], (user_clicks[0] + "_tripleNullRigGrp"))
        cmds.parentConstraint(user_clicks[0], (user_clicks[0] + "_parentConstraint"))
        cmds.parentConstraint(user_clicks[0], (user_clicks[0] + "_animate"))
        cmds.parentConstraint(user_clicks[0], (user_clicks[0] + "_childConstraint"))

        #Parenting each circle, from inner to outer and putting them into the empty group
        cmds.parent("tempLocator", (user_clicks[0] + "_tripleNullRigGrp"))
        cmds.parent((user_clicks[0] + "_parentConstraint"), (user_clicks[0]+"_tripleNullRigGrp"))
        cmds.parent((user_clicks[0] + "_animate"), (user_clicks[0]+"_parentConstraint"))
        cmds.parent((user_clicks[0] + "_childConstraint"), (user_clicks[0]+"_animate"))

        #Deletes parent constraint connection while maintaining position and getting rid of construction history.
        cmds.delete((user_clicks[0] + "_tripleNullRigGrp"), cn=True)
        cmds.delete((user_clicks[0] + "_parentConstraint"), cn=True, ch=True)
        cmds.delete((user_clicks[0] + "_animate"), cn=True, ch=True)
        cmds.delete((user_clicks[0] + "_childConstraint"), cn=True, ch=True)

        #Removes the temp locator
        cmds.delete("tempLocator")
    else:
        print("Select exactly 1 object/controller to create rig")

    return user_clicks[0]

triple_null_rig()

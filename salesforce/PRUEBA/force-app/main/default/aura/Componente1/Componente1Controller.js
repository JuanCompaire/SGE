({
    myAction : function(component, event, helper) {
        



    },
    addNumber1 : function(component, event, helper) {
        var evt = $A.get("e.c:evtData");
        var obj ={
            "number" : "1"
        }
        evt.setParams(obj);
        evt.fire();

    },
    addNumber2 : function(component, event, helper) {
        var evt = $A.get("e.c:evtData");
        var obj ={
            "number" : "2"
        }
        evt.setParams(obj);
        evt.fire();

    },
    addNumber3 : function(component, event, helper) {
        var evt = $A.get("e.c:evtData");
        var obj ={
            "number" : "3"
        }
        evt.setParams(obj);
        evt.fire();

    },
   
})

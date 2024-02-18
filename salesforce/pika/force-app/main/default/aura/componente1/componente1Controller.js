({
    djdhfsjdj: function(component, event, helper) {
        },
    saludar : function(component, event, helper) {
        alert("antes eras "+ component.get("v.nombreOld")+" y ahora eres "+ component.get("v.nombre"));
        component.set("v.nombre", "Alert!");
        //triggers an event
        var evt = $A.get("e.c:evtData");
        var obj ={
            "nombre" : component.get("v.nombre"),
            "apellido" : "Alert!",
        };
        evt.setParams(obj);
        component.set("v.nombreOld", component.get("v.nombre"));
        evt.fire();
    }
})

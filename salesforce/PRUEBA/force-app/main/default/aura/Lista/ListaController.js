({
    myAction : function(component, event, helper) {

    },
    addToList : function(component, event, helper) {
        var lista = component.get("v.lista");
        var item = event.getParam("number");
        lista.push(item);
        component.set("v.lista", lista);
    },
    clearList: function(component, event, helper) {
        component.set("v.lista", []);
    }
})

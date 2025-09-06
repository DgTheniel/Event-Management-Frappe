
frappe.ui.form.on("Venue", {
    validate: function(frm) {
        if (frm.doc.capacity && frm.doc.capacity <= 0) {
            frappe.throw(__("Capacity must be greater than 0"));
        }
    }
});

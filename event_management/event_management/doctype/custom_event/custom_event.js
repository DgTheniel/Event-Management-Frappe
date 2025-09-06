frappe.ui.form.on("Custom Event", {
    validate: function(frm) {
        if (frm.doc.capacity && frm.doc.capacity <= 0) {
            frappe.throw(__("Capacity must be greater than 0"));
        }
        if (frm.doc.start_date && frm.doc.end_date && frm.doc.end_date < frm.doc.start_date) {
            frappe.throw(__("End Date must be after Start Date"));
        }
    }
});

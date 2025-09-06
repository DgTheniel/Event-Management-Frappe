import frappe
from frappe.model.document import Document
from frappe import _

class CustomEvent(Document):
    def validate(self):
        # Ensure capacity is positive
        if self.capacity is not None and self.capacity <= 0:
            frappe.throw(_("Capacity must be greater than 0"))

        # Check that end date is after start date
        if self.start_date and self.end_date:
            if self.end_date < self.start_date:
                frappe.throw(_("End Date must be after Start Date"))
        
        # Status must be one of allowed options
        if self.status and self.status not in ["Draft", "Scheduled", "Completed", "Cancelled"]:
            frappe.throw(_("Invalid Status selected"))

        # Venue must be linked (optional, only if you want mandatory check)
        if not self.venue:
            frappe.throw(_("Please select a Venue"))

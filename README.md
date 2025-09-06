# Event Management System

A **Frappe Framework-based Event Management System** to manage events and venues efficiently, with full CRUD operations, validations, and relational links.

---

## Features

### Custom Event
- Create, view, edit, and delete events.  
- **Fields include:** Event Name, Description, Start/End Dates, Venue, Capacity.  
- **Validations:**
  - End Date must be after Start Date.
  - Event capacity cannot exceed venue capacity.  
- Venue linkage ensures events are assigned to proper venues.

### Venue
- Manage venues with: Venue Name, Address, Capacity, Email, Phone, Coordinates.  
- **Validations:**
  - Capacity must be greater than 0.
  - Email format validation.
  - Phone must be 10 digits.  
- Coordinates optional for mapping.

### System
- Fully functional CRUD interface via **Frappe Desk**.  
- List views with filters for events and venues.  
- Supports client-side validations for enhanced usability.

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/DgTheniel/Event-Management-Frappe.git
cd event_management
```

2. Set up Frappe environment and site (see [Frappe Docs](https://docs.frappe.io/framework/user/en/installation)):

```bash
bench --site your-site-name migrate
bench start
```

3. Access the system:

```
http://localhost:8000
```

---

## Usage

- Add **venues** first.  
- Create **events** linking them to venues.  
- Use list view filters to sort events by date, venue, or capacity.  
- Validate inputs according to system rules.

---

## Tech Stack

- **Backend & Framework:** Frappe Framework (Python)  
- **Frontend:** Frappe Desk (optional React integration)  
- **Database:** MariaDB  
- **Cache & Queue:** Redis  

---

## Screenshots

Screenshots of working forms and list views are included in the `screenshots/` folder.

---

## Challenges Faced

- Setting up custom DocTypes from scratch and linking them correctly.  
- Validating relational fields like Venue in Event.  
- Learning Frappe Desk interface quickly and implementing proper client-side validations.  

---

## Author

**DG Theniel**  
GitHub: [https://github.com/DgTheniel](https://github.com/DgTheniel)

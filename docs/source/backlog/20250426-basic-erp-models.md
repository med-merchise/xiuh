# Models for a mini ERP

Initially, the models are developed using a Service Workshop as a Business
Type.

## Models

### Work Orders

Central record for repair or maintenance jobs.

**Columns:**
- Work Order ID (unique identifier)
- Truck/Vehicle ID
- License Plate
- Customer Name (or "Client Name")
- Customer Contact
- Date Received (or "Date Opened")
- Date Promised
- Current Status (or just "Status")
  - `New`, `In Progress`, `Completed`, `Delivered`
- Problem Description (or "Issue Description")
- Diagnostic Notes
- Estimated Labor Hours
- Estimated Parts Cost
- Estimated Total Cost (or only one attribute "Estimated Cost")
- Actual Labor Hours
- Actual Parts Cost
- Actual Total Cost (or only one attribute "Final Cost")
- Final Price Charged
- Profit Margin
- Technician Assigned (or "Assigned Technician")
- Approval Signature
- Completion Date
- Delivery Date
- Payment Status
- Notes

### Work Reports

Summarizes what was done in each "Work Order", linking parts and labor.

**Columns:**
- Report ID
- Work Order ID (linked)
- Date (or "Completion Date")
- Technician Name (or "Technician", must be linked)
- Work Performed (or "Task Description")
- Hours Worked
- Parts Used (linked, "SKU" + "Quantities")
- Labor Entries (linked, "Hourly Rate"}
- Customer Approval/Signature
- Total Parts Cost {added}
- Total Labor Cost {added}
- Total Cost {added}
- Billed Amount {added}
- Final Price Charged {added}
- Notes {added, was "Additional Notes"}
- Photos/Documents (hyperlink)

### Inventory (Parts)

Tracks all parts used in repairs and their related financial transactions.

**Columns:**
- SKU (unique identifier)
- Part Name
- Description
- Category: "Engine", "Brakes", "Electrical", etc.
- Status "Active", "Discontinued"
- Vehicle Compatibility
- Supplier ID (linked to Suppliers sheet)
- Current Stock (or "Quantity in Stock")
- Minimum Stock Level
- Reorder Quantity (or "Reorder Level")
- Unit Cost (from supplier)
- Unit Price
- Storage Location
- Last Purchase Date
- Lead Time (days)
- Markup Percentage
  - See [parts-markup].
- Selling Price (calculated)
- Total Value (or "Total Cost"): `Current Stock × Unit Cost`
- Notes

### Suppliers

**Columns:**
- Supplier ID
- Supplier Name
- Contact Person
- Phone
- Email
- Address
- Primary Parts Supplied
- Payment Terms
- Average Lead Time
- Rating (1-5)
- Notes
- Tax ID

### Purchase Requests

Handles both **planned** and **emergency** requests for parts.

**Columns:**
- Request ID
- Type: "Planned", "Emergency"
- Date Requested (or "Request Date", "Order Date")
- Received Date
- Priority: "Low", "Medium", "High", "Critical" (or "Planned", "Emergency")
- Requested By
- Approval Status
- Approved By
- Approval Date
- Expected Delivery Date
- Items: Linked to Parts (`SKU`) + "Quantity" (many to many)
- Estimated Cost
- Supplier (linked)
- Associated Work Order (if emergency)
- Notes

### Labors

**Columns:**
- Labor Code
- Service Description
- Standard Hours
- Skill Level Required
- Hourly Cost Rate
- Markup Percentage
  - See [parts-markup].
- Customer Charge Rate (calculated)
- Category: "Diagnostic", "Repair", "Maintenance"
- Notes

### Employees/Technicians

**Columns:**
- Employee ID
- Name
- Position
- Contact Info
- Hire Date
- Hourly Rate
- Skill Certifications
- Availability
- Performance Metrics
- Notes

## Cost & Price Management Summary

**Columns:**
- Date Range
- Total Parts Cost
- Total Labor Cost
- Overhead Costs
- Total Expenses
- Total Revenue
- Gross Profit
- Profit Margin
- Most Used Parts
- Most Performed Services
- Technician Productivity

## Implementation Notes:

1. **Formulas to Include:**
   - Automatic price calculations `(cost × markup)`.
   - Inventory alerts when stock is low.
   - Profit calculations on work orders.
   - Labor cost calculations based on `hours × rate`.

2. **Data Validation:**
   - Dropdown lists for statuses, categories, and other standardized fields.
   - Unique identifiers for all key records.

3. **Visual Indicators:**
   - Conditional formatting for overdue work orders.
   - Color coding for emergency purchase requests.
   - Stock level warnings.

4. **Reporting:**
   - Monthly cost/profit reports.
   - Technician productivity reports.
   - Inventory turnover reports.
   - Supplier performance reports.

This design provides a comprehensive system that tracks all aspects of your
truck repair shop operations while maintaining focus on cost control and
pricing management.  The sheets can be linked through `ID` fields to maintain
data integrity and provide complete visibility from work order through to
final invoicing.

let passengers = [];
let flights = [];
let tickets = [];

function showDashboard(dashboardId) {
  const dashboards = document.querySelectorAll('.dashboard');
  dashboards.forEach(dashboard => {
    dashboard.classList.remove('active');
  });
  
  document.getElementById(dashboardId + 'Dashboard').classList.add('active');
  
  document.querySelectorAll('.dashboard-btn').forEach(btn => {
    btn.classList.remove('active');
  });
  document.getElementById(dashboardId + 'DashboardBtn').classList.add('active');
  
  if (dashboardId === 'view') {
    refreshAllData();
  }
}

function showTab(tabId) {
  const dashboardType = tabId.includes('-entry') ? 'entry' : 'view';
  
  const tabContents = document.querySelectorAll(`#${dashboardType}Dashboard .tab-content`);
  tabContents.forEach(tab => {
    tab.classList.remove('active');
  });
  
  document.getElementById(tabId).classList.add('active');
  
  const tabBtns = document.querySelectorAll(`#${dashboardType}Dashboard .tab-btn`);
  tabBtns.forEach((btn, index) => {
    if (index === Array.from(tabBtns).findIndex(btn => btn.onclick.toString().includes(tabId))) {
      btn.classList.add('active');
    } else {
      btn.classList.remove('active');
    }
  });
}

document.getElementById('passengerForm').addEventListener('submit', function(e) {
  e.preventDefault();
  const formData = new FormData(e.target);
  const passenger = {
    id: Date.now(),
    name: formData.get('name'),
    passport: formData.get('passport'),
    nationality: formData.get('nationality'),
    gender: formData.get('gender'),
    dob: formData.get('dob')
  };
  
  // Add to array and update display
  passengers.push(passenger);
  e.target.reset();
  alert('Passenger added successfully!');
  refreshPassengerTable();
});

document.getElementById('flightForm').addEventListener('submit', function(e) {
  e.preventDefault();
  const formData = new FormData(e.target);
  const flight = {
    id: Date.now(),
    airline_id: formData.get('airline_id'),
    source: formData.get('source'),
    destination: formData.get('destination'),
    departure_time: formData.get('departure_time'),
    arrival_time: formData.get('arrival_time'),
    status: formData.get('status')
  };
  
  // Add to array and update display
  flights.push(flight);
  e.target.reset();
  alert('Flight added successfully!');
  refreshFlightTable();
});

document.getElementById('ticketForm').addEventListener('submit', function(e) {
  e.preventDefault();
  const formData = new FormData(e.target);
  const ticket = {
    id: Date.now(),
    passenger_id: formData.get('passenger_id'),
    flight_id: formData.get('flight_id'),
    seat_number: formData.get('seat_number'),
    class: formData.get('class'),
    price: formData.get('price'),
    booking_date: formData.get('booking_date')
  };
  
  tickets.push(ticket);
  e.target.reset();
  alert('Ticket booked successfully!');
  refreshTicketTable();
});

function refreshAllData() {
  refreshPassengerTable();
  refreshFlightTable();
  refreshTicketTable();
}

function refreshPassengerTable() {
  const list = document.getElementById('passengerList');
  list.innerHTML = '';
  
  passengers.forEach(passenger => {
    const row = document.createElement('tr');
    row.innerHTML = `
      <td>${passenger.id}</td>
      <td>${passenger.name}</td>
      <td>${passenger.passport}</td>
      <td>${passenger.nationality}</td>
      <td>${passenger.gender}</td>
      <td>${passenger.dob}</td>
      <td>
        <button onclick="editPassenger(${passenger.id})">Edit</button>
        <button onclick="deletePassenger(${passenger.id})">Delete</button>
      </td>
    `;
    list.appendChild(row);
  });
}

function refreshFlightTable() {
  const list = document.getElementById('flightList');
  list.innerHTML = '';
  
  flights.forEach(flight => {
    const row = document.createElement('tr');
    row.innerHTML = `
      <td>${flight.id}</td>
      <td>${flight.airline_id}</td>
      <td>${flight.source}</td>
      <td>${flight.destination}</td>
      <td>${flight.departure_time}</td>
      <td>${flight.arrival_time}</td>
      <td>${flight.status}</td>
      <td>
        <button onclick="editFlight(${flight.id})">Edit</button>
        <button onclick="deleteFlight(${flight.id})">Delete</button>
      </td>
    `;
    list.appendChild(row);
  });
}

function refreshTicketTable() {
  const list = document.getElementById('ticketList');
  list.innerHTML = '';
  
  tickets.forEach(ticket => {
    const passenger = passengers.find(p => p.id == ticket.passenger_id) || { name: 'Unknown' };
    const flight = flights.find(f => f.id == ticket.flight_id) || { airline_id: 'Unknown' };
    
    const row = document.createElement('tr');
    row.innerHTML = `
      <td>${ticket.id}</td>
      <td>${passenger.name}</td>
      <td>${flight.airline_id}</td>
      <td>${ticket.seat_number}</td>
      <td>${ticket.class}</td>
      <td>${ticket.price}</td>
      <td>${ticket.booking_date}</td>
      <td>
        <button onclick="editTicket(${ticket.id})">Edit</button>
        <button onclick="deleteTicket(${ticket.id})">Delete</button>
      </td>
    `;
    list.appendChild(row);
  });
}

function editPassenger(id) {
  alert('Edit passenger with ID: ' + id);
}

function deletePassenger(id) {
  if(confirm('Are you sure you want to delete this passenger?')) {
    passengers = passengers.filter(p => p.id !== id);
    refreshPassengerTable();
  }
}

function editFlight(id) {
  alert('Edit flight with ID: ' + id);
}

function deleteFlight(id) {
  if(confirm('Are you sure you want to delete this flight?')) {
    flights = flights.filter(f => f.id !== id);
    refreshFlightTable();
  }
}

function editTicket(id) {
  alert('Edit ticket with ID: ' + id);
}

function deleteTicket(id) {
  if(confirm('Are you sure you want to delete this ticket?')) {
    tickets = tickets.filter(t => t.id !== id);
    refreshTicketTable();
  }
}

window.onload = function() {
  showDashboard('entry');
  document.querySelector('#entryDashboard .tab-btn').classList.add('active');
  document.querySelector('#viewDashboard .tab-btn').classList.add('active');
  document.getElementById('passengers-entry').classList.add('active');
  document.getElementById('passengers-view').classList.add('active');
};

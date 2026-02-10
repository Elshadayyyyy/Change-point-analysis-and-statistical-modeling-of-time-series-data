import React, { useEffect, useState } from "react";
import axios from "axios";

export default function EventsTable() {
  const [events, setEvents] = useState([]);
  useEffect(() => {
    axios.get("http://localhost:5000/events")
      .then(res => {
        const formatted = JSON.parse(res.data).map(event => ({
          ...event,
          Date: new Date(event.Date).toLocaleDateString()
        }));
        setEvents(formatted);
      })
      .catch(err => console.error("Error fetching events:", err));
  }, []);

  return (
    <div style={{ marginTop: "40px" }}>
      <h2>Key Events Affecting Brent Oil Prices</h2>
      <table style={{ width: "100%", borderCollapse: "collapse" }}>
        <thead>
          <tr>
            <th style={{ border: "1px solid #ccc", padding: "8px" }}>Date</th>
            <th style={{ border: "1px solid #ccc", padding: "8px" }}>Event</th>
          </tr>
        </thead>
        <tbody>
          {events.map((event, index) => (
            <tr key={index}>
              <td style={{ border: "1px solid #ccc", padding: "8px" }}>{event.Date}</td>
              <td style={{ border: "1px solid #ccc", padding: "8px" }}>{event.Event}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

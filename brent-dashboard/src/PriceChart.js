import React, { useEffect, useState } from "react";
import { LineChart, Line, XAxis, YAxis, Tooltip, CartesianGrid, ReferenceLine } from "recharts";
import axios from "axios";

export default function PriceChart() {
  const [data, setData] = useState([]);
  const [changePoints, setChangePoints] = useState([]);
  useEffect(() => {
    axios.get("http://localhost:5000/prices").then(res => setData(res.data));
    axios.get("http://localhost:5000/change_points").then(res => setChangePoints(res.data));
  }, []);
  return (
    <LineChart width={1200} height={500} data={data}>
      <XAxis dataKey="Date" />
      <YAxis />
      <CartesianGrid stroke="#eee" strokeDasharray="5 5" />
      <Tooltip />
      <Line type="monotone" dataKey="Price" stroke="#8884d8" />
      {changePoints.map((cp, i) => (
        <ReferenceLine key={i} x={cp} stroke="red" strokeDasharray="3 3" label={`Change ${i+1}`} />
      ))}
    </LineChart>
  );
}

def test_summary_endpoint(client):
    response = client.get("/summary")
    assert response.status_code == 200
    data = response.get_json()
    assert "total_price_records" in data
    assert "number_of_change_points" in data
    assert "max_price" in data
    assert "min_price" in data

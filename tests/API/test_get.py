def test_get(playwright):
    request = playwright.request.new_context()
    response = request.get("https://jsonplaceholder.typicode.com/todos/1")

    assert response.status == 200
    json_data = response.json()
    print(json_data)

    request.dispose()
    print("Test completed successfully.")
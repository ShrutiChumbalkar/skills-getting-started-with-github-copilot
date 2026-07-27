def test_get_activities_returns_expected_keys(client):
    # Arrange
    # Act
    resp = client.get("/activities")
    # Assert
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, dict)
    assert "Chess Club" in data


def test_signup_success_and_reflected_in_data(client):
    # Arrange
    activity = "Chess Club"
    email = "newstudent@example.com"

    # Act
    resp = client.post(f"/activities/{activity}/signup", params={"email": email})

    # Assert
    assert resp.status_code == 200
    assert email in client.get("/activities").json()[activity]["participants"]


def test_signup_duplicate_returns_400(client):
    # Arrange
    activity = "Chess Club"
    email = "michael@mergington.edu"  # already in initial data

    # Act
    resp = client.post(f"/activities/{activity}/signup", params={"email": email})

    # Assert
    assert resp.status_code == 400


def test_signup_nonexistent_activity_returns_404(client):
    # Act
    resp = client.post("/activities/NoSuchClub/signup", params={"email": "x@y.com"})

    # Assert
    assert resp.status_code == 404


def test_remove_participant_success(client):
    # Arrange
    activity = "Chess Club"
    email = "daniel@mergington.edu"

    # Act
    resp = client.delete(f"/activities/{activity}/participants", params={"email": email})

    # Assert
    assert resp.status_code == 200
    assert email not in client.get("/activities").json()[activity]["participants"]


def test_remove_participant_not_found_returns_404(client):
    # Arrange
    activity = "Chess Club"
    email = "noone@nowhere.edu"

    # Act
    resp = client.delete(f"/activities/{activity}/participants", params={"email": email})

    # Assert
    assert resp.status_code == 404

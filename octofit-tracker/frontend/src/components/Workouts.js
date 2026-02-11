import React, { useState, useEffect } from 'react';

function Workouts() {
  const [workouts, setWorkouts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchWorkouts = async () => {
      try {
        const codespaceName = process.env.REACT_APP_CODESPACE_NAME;
        const apiUrl = codespaceName 
          ? `https://${codespaceName}-8000.app.github.dev/api/workouts/`
          : 'http://localhost:8000/api/workouts/';
        
        console.log('Fetching workouts from:', apiUrl);
        
        const response = await fetch(apiUrl);
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        
        console.log('Workouts data received:', data);
        
        // Handle both paginated (.results) and plain array responses
        const workoutsData = data.results || data;
        setWorkouts(Array.isArray(workoutsData) ? workoutsData : []);
        setLoading(false);
      } catch (err) {
        console.error('Error fetching workouts:', err);
        setError(err.message);
        setLoading(false);
      }
    };

    fetchWorkouts();
  }, []);

  if (loading) return (
    <div className="container mt-4">
      <div className="text-center py-5">
        <div className="spinner-border text-primary" role="status">
          <span className="visually-hidden">Loading...</span>
        </div>
        <p className="mt-3">Loading workouts...</p>
      </div>
    </div>
  );
  
  if (error) return (
    <div className="container mt-4">
      <div className="alert alert-danger" role="alert">
        <h4 className="alert-heading">Error!</h4>
        <p className="mb-0">{error}</p>
      </div>
    </div>
  );

  const getDifficultyBadge = (difficulty) => {
    const level = difficulty?.toLowerCase();
    if (level === 'easy' || level === 'beginner') return 'bg-success';
    if (level === 'medium' || level === 'intermediate') return 'bg-warning';
    if (level === 'hard' || level === 'advanced') return 'bg-danger';
    return 'bg-secondary';
  };

  return (
    <div className="container mt-4">
      <div className="d-flex justify-content-between align-items-center mb-4">
        <h2>💪 Workout Suggestions</h2>
        <span className="badge bg-primary">{workouts.length} Workouts</span>
      </div>
      <div className="row">
        {workouts.length > 0 ? (
          workouts.map((workout) => (
            <div key={workout.id} className="col-md-6 col-lg-4 mb-4">
              <div className="card h-100">
                <div className="card-header bg-primary text-white">
                  <h5 className="mb-0">{workout.name}</h5>
                </div>
                <div className="card-body">
                  <p className="card-text text-muted">{workout.description}</p>
                  <hr />
                  <ul className="list-group list-group-flush">
                    <li className="list-group-item d-flex justify-content-between align-items-center">
                      <strong>Type:</strong>
                      <span className="badge bg-info">
                        {workout.workout_type || workout.type}
                      </span>
                    </li>
                    <li className="list-group-item d-flex justify-content-between align-items-center">
                      <strong>Duration:</strong>
                      <span className="badge bg-secondary">
                        ⏱️ {workout.duration} min
                      </span>
                    </li>
                    <li className="list-group-item d-flex justify-content-between align-items-center">
                      <strong>Difficulty:</strong>
                      <span className={`badge ${getDifficultyBadge(workout.difficulty_level || workout.difficulty)}`}>
                        {workout.difficulty_level || workout.difficulty}
                      </span>
                    </li>
                    {workout.calories_estimate && (
                      <li className="list-group-item d-flex justify-content-between align-items-center">
                        <strong>Calories:</strong>
                        <span className="badge bg-success">
                          🔥 ~{workout.calories_estimate}
                        </span>
                      </li>
                    )}
                  </ul>
                </div>
                <div className="card-footer bg-light">
                  <button className="btn btn-success w-100">Start Workout</button>
                </div>
              </div>
            </div>
          ))
        ) : (
          <div className="col-12">
            <div className="alert alert-info" role="alert">
              <p className="text-center mb-0">No workout suggestions available</p>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

export default Workouts;

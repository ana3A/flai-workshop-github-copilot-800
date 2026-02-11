import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import './App.css';
import Activities from './components/Activities';
import Leaderboard from './components/Leaderboard';
import Teams from './components/Teams';
import Users from './components/Users';
import Workouts from './components/Workouts';

function App() {
  return (
    <Router>
      <div className="App">
        <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
          <div className="container-fluid">
            <Link className="navbar-brand" to="/">
              <img 
                src="/octofitapp-small.png" 
                alt="OctoFit Logo" 
                className="navbar-logo"
              />
              OctoFit Tracker
            </Link>
            <button 
              className="navbar-toggler" 
              type="button" 
              data-bs-toggle="collapse" 
              data-bs-target="#navbarNav" 
              aria-controls="navbarNav" 
              aria-expanded="false" 
              aria-label="Toggle navigation"
            >
              <span className="navbar-toggler-icon"></span>
            </button>
            <div className="collapse navbar-collapse" id="navbarNav">
              <ul className="navbar-nav">
                <li className="nav-item">
                  <Link className="nav-link" to="/users">Users</Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/activities">Activities</Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/teams">Teams</Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/leaderboard">Leaderboard</Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/workouts">Workouts</Link>
                </li>
              </ul>
            </div>
          </div>
        </nav>

        <Routes>
          <Route path="/" element={
            <div className="container mt-4">
              <div className="card">
                <div className="card-body text-center py-5">
                  <h1 className="mb-4">Welcome to OctoFit Tracker</h1>
                  <p className="lead mb-4">Track your fitness activities, compete with your team, and reach your goals!</p>
                  <div className="row mt-4">
                    <div className="col-md-4 mb-3">
                      <Link to="/users" className="text-decoration-none">
                        <div className="card bg-light card-hover">
                          <div className="card-body">
                            <h5 className="card-title">👥 Users</h5>
                            <p className="card-text">View and manage user profiles</p>
                          </div>
                        </div>
                      </Link>
                    </div>
                    <div className="col-md-4 mb-3">
                      <Link to="/activities" className="text-decoration-none">
                        <div className="card bg-light card-hover">
                          <div className="card-body">
                            <h5 className="card-title">📊 Activities</h5>
                            <p className="card-text">Log and monitor your daily fitness activities</p>
                          </div>
                        </div>
                      </Link>
                    </div>
                    <div className="col-md-4 mb-3">
                      <Link to="/leaderboard" className="text-decoration-none">
                        <div className="card bg-light card-hover">
                          <div className="card-body">
                            <h5 className="card-title">🏆 Leaderboard</h5>
                            <p className="card-text">See the top performers and compete with others</p>
                          </div>
                        </div>
                      </Link>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          } />
          <Route path="/users" element={<Users />} />
          <Route path="/activities" element={<Activities />} />
          <Route path="/teams" element={<Teams />} />
          <Route path="/leaderboard" element={<Leaderboard />} />
          <Route path="/workouts" element={<Workouts />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;

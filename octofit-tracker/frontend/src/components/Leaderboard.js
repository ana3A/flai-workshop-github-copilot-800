import React, { useState, useEffect } from 'react';

function Leaderboard() {
  const [leaderboard, setLeaderboard] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchLeaderboard = async () => {
      try {
        const codespaceName = process.env.REACT_APP_CODESPACE_NAME;
        const apiUrl = codespaceName 
          ? `https://${codespaceName}-8000.app.github.dev/api/leaderboard/`
          : 'http://localhost:8000/api/leaderboard/';
        
        console.log('Fetching leaderboard from:', apiUrl);
        
        const response = await fetch(apiUrl);
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        
        console.log('Leaderboard data received:', data);
        
        // Handle both paginated (.results) and plain array responses
        const leaderboardData = data.results || data;
        setLeaderboard(Array.isArray(leaderboardData) ? leaderboardData : []);
        setLoading(false);
      } catch (err) {
        console.error('Error fetching leaderboard:', err);
        setError(err.message);
        setLoading(false);
      }
    };

    fetchLeaderboard();
  }, []);

  if (loading) return (
    <div className="container mt-4">
      <div className="text-center py-5">
        <div className="spinner-border text-primary" role="status">
          <span className="visually-hidden">Loading...</span>
        </div>
        <p className="mt-3">Loading leaderboard...</p>
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

  const getRankBadge = (rank) => {
    if (rank === 1) return <span className="badge bg-warning text-dark">🥇 1st</span>;
    if (rank === 2) return <span className="badge bg-secondary">🥈 2nd</span>;
    if (rank === 3) return <span className="badge bg-danger">🥉 3rd</span>;
    return <span className="badge bg-primary">{rank}th</span>;
  };

  return (
    <div className="container mt-4">
      <div className="d-flex justify-content-between align-items-center mb-4">
        <h2>🏆 Leaderboard</h2>
        <span className="badge bg-primary">{leaderboard.length} Competitors</span>
      </div>
      <div className="table-responsive">
        <table className="table table-striped table-hover">
          <thead>
            <tr>
              <th>Rank</th>
              <th>Name</th>
              <th>Team</th>
              <th>Total Points</th>
              <th>Activities</th>
            </tr>
          </thead>
          <tbody>
            {leaderboard.length > 0 ? (
              leaderboard.map((entry, index) => (
                <tr key={entry.id || index} className={index < 3 ? 'table-active' : ''}>
                  <td>{getRankBadge(index + 1)}</td>
                  <td><strong>{entry.name || entry.username}</strong></td>
                  <td>
                    <span className="badge bg-info">{entry.team || 'N/A'}</span>
                  </td>
                  <td>
                    <span className="badge bg-success" style={{fontSize: '1rem'}}>
                      {entry.total_points || entry.points || 0} pts
                    </span>
                  </td>
                  <td>
                    <span className="badge bg-secondary">
                      {entry.activities_count || entry.activity_count || 0}
                    </span>
                  </td>
                </tr>
              ))
            ) : (
              <tr>
                <td colSpan="5" className="text-center py-4">
                  <p className="text-muted mb-0">No leaderboard data available</p>
                </td>
              </tr>
            )}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default Leaderboard;

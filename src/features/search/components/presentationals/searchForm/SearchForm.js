import React from "react";

class SearchForm extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      text: ""
    };
  }
  onChange = event => {
    this.setState({
      text: event.target.value
    });
  };
  onSubmit = event => {
    event.preventDefault();
  };
  render() {
    return (
      <div className="form container">
        <form onSubmit={this.onSubmit}>
          <div className="field">
            <div className="control">
              <input
                name="text"
                placeholder="Code postal, ville, département ..."
                value={this.state.text}
                onChange={this.onChange}
                className="input"
                type="text"
              />
            </div>
          </div>
          <div className="field">
            <div className="control">
              <button className="button is-primary">OK</button>
            </div>
          </div>
        </form>
      </div>
    );
  }
}

export default SearchForm;
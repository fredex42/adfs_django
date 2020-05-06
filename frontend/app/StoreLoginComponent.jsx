import React from 'react';
import {withRouter} from 'react-router-dom';
import {Redirect} from "react-router-dom";

/**
 * component that responds to a /logged_in endpoint.
 * it extracts a JWT from the query string and stores it in the session
 */
class StoreLoginComponent extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            lastError: null,
            haveStored: false,
        }
    }

    componentDidMount() {
        try {
            const queryString = this.props.location.search;
            const qsParts = queryString.split("&")
            const queryParams = qsParts.reduce((acc,elem)=>{
                const elemParts = elem.split('=');
                let newItem = {};
                newItem[elemParts[0]] = elemParts[1]
                return Object.assign(acc, newItem);
            });

            console.log(queryParams)
            sessionStorage.setItem("adfs-django:jwt", queryParams.token)
            this.setState({haveStored: true})
        } catch(e) {
            console.error(e);
            this.setState({lastError: e.toString()})
        }
    }

    render() {
        if(this.state.haveStored) {
            return <Redirect to="/"/>
        } else {
            return <div>
                <h2>Logging in</h2>
                <p style={{display: this.state.lastError ? "none" : "inherit"}}>Authentication completed, storing token...</p>
                <p className="error" style={{display: this.state.lastError ? "inherit" : "none"}}>Could not store: {this.state.lastError}</p>
            </div>
        }
    }
}

export default StoreLoginComponent;
import React from 'react';

class RestTestComponent extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            loading: false,
            lastError: null,
            receivedData: {}
        }
    }

    setStatePromise(newState) {
        return new Promise((resolve, reject)=>{try{
            this.setState(newState, ()=>resolve())
        } catch(e){ reject(e) }})
    }

    async componentDidMount() {
        const bearerToken = sessionStorage.getItem("adfs-django:jwt");
        if(bearerToken===null || bearerToken==="") {
            return this.setStatePromise({loading: false, lastError: "Not logged in, no token"});
        }
        await this.setStatePromise({loading: true});
        const response = await fetch("/api/test",{headers: {Authorization: "JWT " + bearerToken}});
        if(response.status===200){
            const data = await response.json();
            return this.setStatePromise({loading: false, receivedData: data});
        } else {
            const errorText = await response.text();
            try {
                const errorData = JSON.parse(errorText);
                return this.setStatePromise({loading: false, lastError: errorText})
            } catch (e) {
                return this.setStatePromise({loading: false, lastError: errorText});
            }
        }
    }

    render() {
        return <div>
            <h2>REST test</h2>
            <p style={{display: this.state.loading ? "inherit": "none"}}>loading....</p>
            <h4>Received data:</h4>
            <ul>{
                Object.keys(this.state.receivedData).map((k,i)=><li key={i}>{k}: {this.state.receivedData[k]}</li>)
            }
            <li style={{display: Object.keys(this.state.receivedData).length>0 ? "none" : "inherit"}}>No data</li>
            </ul>

            <p style={{display: this.state.lastError ? "inherit" : "none"}} className="error">{this.state.lastError}</p>
        </div>
    }
}

export default RestTestComponent;
import React, { Component } from 'react'
import axios from 'axios'

class CreatePhrase extends Component {
    constructor(props) {
        super(props)

        this.state = {
            fullname: '',
            zip: ''
        }
    }

    changeHandler = (e) => {
        this.setState({ [e.target.name]: e.target.value })
    }

    submitHandler= e => {
        e.preventDefault()
        console.log(this.state)
        axios.post('localhost:3000', this.state)
            .this(response => {
                console.log(response)
            })
            .catch(error => {
                console.log(error)
            })
    }

    render() {
        const { fullname, zip } = this.state
        return (
            <div>
                <form onSubmit={this.submitHandler}  class="form-signin" method="POST" action="/create_phrase">
                    <div class="form-signin-heading">
                        <input type="text" name="fullname" value={fullname} onChange={this.changeHandler} />
                    </div>
                    <div class="form-signin-heading">
                        <input type="text" name="zip" value={zip} onChange={this.changeHandler} />
                    </div>
                    {/* <button type='submit'>Submit</button> */}
                    <button class="btn btn-lg btn-primary btn-block" type="submit">Create Phrase</button>
                </form>
            </div>
        )
    }
}

export default CreatePhrase
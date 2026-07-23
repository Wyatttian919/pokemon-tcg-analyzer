import { Outlet } from "react-router-dom";

import Navbar from "./Navbar";

import "../styles/layout.css";


function Layout(){

    return (

        <>

            <Navbar />


            <main className="page-container">

                <Outlet />

            </main>


        </>

    );

}


export default Layout;
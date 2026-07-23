import {
    BrowserRouter,
    Routes,
    Route
} from "react-router-dom";


import SearchPage from "./pages/SearchPage";
import CardDetailPage from "./pages/CardDetailPage";
import CollectionPage from "./pages/CollectionPage";
import Navbar from "./components/Navbar";
import Layout from "./components/Layout";


function App() {

    return (

        <BrowserRouter>


            <Navbar />
            

            <Routes>


                <Route
                    element={<Layout />}

                ></Route>


                

                <Route
                    path="/"
                    element={<SearchPage />}
                />


                <Route
                    path="/cards/:id"
                    element={<CardDetailPage />}
                />



                <Route
                    path="/collection"
                    element={<CollectionPage />}
                />

            </Routes>

        </BrowserRouter>

    );

}


export default App;
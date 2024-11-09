import { Loader } from "lucide-react";

export default function Loading() {
  return (
    <div className="w-full h-screen flex justify-center items-center"><Loader size={32} className="animate-spin"/></div>
  )
}
